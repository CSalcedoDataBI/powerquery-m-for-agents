#!/usr/bin/env python3
"""Regenerate m-reference/generated/ from one or more #shared exports.

The upstream is the engine itself: export_shared.pq dumps every function #shared holds,
with the documentation metadata on its type, as JSON. Each export is one host (Desktop,
Excel, Dataflows Gen2). This script merges them:

  - a function's card comes from the first export (in argument order) that has it;
  - its `hosts` field lists every export it appears in;
  - it is flagged ⌂ when it is missing from at least one of them.

The functions are split into two indexes, both backed by the same cards:

  - catalog.md    the language library;
  - connectors.md connector entry points (`Mixpanel.Tables`, `Stripe.Contents`, ...).

A connector is a function the engine gives no Documentation.Category whose prefix no
categorised function shares. The core library documents its category; connectors shipped
as extensions mostly do not. "Accessing data" (Csv.Document, Web.Contents, ...) is a
documented library category, so it stays in catalog.md.

The non-function members of #shared (GroupKind.Local, JoinKind.Inner, Int64.Type, ...)
go to constants.md, merged across hosts the same way. They have no cards: one row says it
all. An export taken before the query exported constants simply contributes none.

Everything under generated/ is replaced wholesale. notes/ and examples/ are read to set
the ★ and ▶ flags and are never written.

Gates, all checked before anything is written:
  - an export with fewer than --min-functions functions (wrong query, wrong host);
  - two functions that map to the same card filename;
  - a notes/<file>.md with no card;
  - the function count moving more than 5% from the last catalog.json, unless
    --accept-count-change.

Run:
  python sync_shared.py exports/desktop-2.140.json exports/excel-16.0.json          # report
  python sync_shared.py exports/desktop-2.140.json exports/excel-16.0.json --write  # write
"""
import argparse
import html
import json
import os
import re
import shutil
import sys

REF = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COUNT_TOLERANCE = 0.05
MIN_FUNCTIONS = 100
SUMMARY_CHARS = 120
# A constant's first sentence is often the same for the whole enum ("A possible value for
# the optional JoinKind parameter in Table.Join."), so its row keeps more of the text.
CONSTANT_SUMMARY_CHARS = 200


class GateError(Exception):
    """A generation that must not be written."""


def card_file(name):
    """`Table.AddColumn` -> `table-addcolumn`; `#date` -> `hash-date`."""
    stem = name.lower()
    if stem.startswith("#"):
        stem = "hash-" + stem[1:]
    return re.sub(r"[^a-z0-9]+", "-", stem).strip("-")


def category_slug(category):
    return re.sub(r"[^a-z0-9]+", "-", category.lower()).strip("-") or "uncategorised"


def category_of(fn):
    """The engine's own category, else the prefix before the dot, else '(none)'."""
    if fn.get("category"):
        return fn["category"]
    name = fn["name"]
    return name.split(".", 1)[0] if "." in name else "(none)"


def library_prefixes(functions):
    """Prefixes of the functions the engine categorised: `Table`, `List`, `Csv`, ..."""
    return {fn["name"].split(".", 1)[0] for fn in functions if fn.get("category")}


def kind_of(fn, prefixes):
    """'connector' for an uncategorised `Vendor.Function` whose vendor is not a library
    prefix; 'library' otherwise. `#date` has no dot and stays in the library."""
    name = fn["name"]
    if fn.get("category") or "." not in name:
        return "library"
    return "library" if name.split(".", 1)[0] in prefixes else "connector"


def load_export(path):
    """One export as a dict. Accepts the concatenated payload or the raw chunk table."""
    with open(path, encoding="utf-8-sig") as f:
        data = json.load(f)
    if isinstance(data, list) and data and isinstance(data[0], dict) and "part" in data[0]:
        data = json.loads("".join(c["json"] for c in sorted(data, key=lambda c: c["part"])))
    if not isinstance(data, dict) or not isinstance(data.get("functions"), list):
        raise GateError(f"{path}: not an export_shared.pq payload (no 'functions' list)")
    data.setdefault("host", os.path.splitext(os.path.basename(path))[0])
    return data


def clean_text(text):
    """The engine's Documentation.* strings are HTML fragments indented for a C# source
    file. Four leading spaces make a Markdown code block, so the indentation goes too."""
    if not text:
        return ""
    t = re.sub(r"<code>\s*(.*?)\s*</code>", r"`\1`", text, flags=re.S | re.I)
    t = re.sub(r"<br\s*/?>|</?p\s*>|</?div\s*>|</tr\s*>|</?ul\s*>", "\n", t, flags=re.I)
    t = re.sub(r"<li\s*>", "\n- ", t, flags=re.I)
    t = re.sub(r"</li\s*>", "", t, flags=re.I)
    t = re.sub(r"</td\s*>", " ", t, flags=re.I)
    t = re.sub(r"</?(b|strong)\s*>", "**", t, flags=re.I)
    t = re.sub(r"</?(i|em)\s*>", "*", t, flags=re.I)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t).replace("\xa0", " ")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in t.splitlines()]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def signature(fn):
    parts = []
    for p in fn.get("parameters") or []:
        prefix = "optional " if p.get("optional") else ""
        parts.append(f"{prefix}{p['name']} as {p.get('type') or 'any'}")
    return f"{fn['name']}({', '.join(parts)}) as {fn.get('returns') or 'any'}"


def truncate(text, limit):
    if len(text) > limit:
        text = text[:limit - 1].rstrip() + "…"
    return text.replace("|", "\\|")


def summary(fn):
    text = clean_text(fn.get("description") or fn.get("longDescription"))
    text = re.sub(r"\s+", " ", text)
    return truncate(re.split(r"(?<=\.)\s", text, maxsplit=1)[0], SUMMARY_CHARS)


def constant_summary(const):
    return truncate(re.sub(r"\s+", " ", clean_text(const.get("description"))),
                    CONSTANT_SUMMARY_CHARS)


def stems(directory):
    if not os.path.isdir(directory):
        return set()
    return {os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith(".md")}


def example_count(ref, category, file):
    path = os.path.join(ref, "examples", category_slug(category), f"{file}.md")
    if not os.path.isfile(path):
        return 0
    with open(path, encoding="utf-8") as f:
        return len(re.findall(r"^```m\s*$", f.read(), re.M))


def merge(exports, min_functions):
    hosts = [e["host"] for e in exports]
    merged = {}
    for export in exports:
        usable = [fn for fn in export["functions"]
                  if isinstance(fn, dict) and fn.get("name") and not fn.get("exportError")]
        if len(usable) < min_functions:
            raise GateError(f"export '{export['host']}' has {len(usable)} functions, "
                            f"fewer than {min_functions}. Wrong query or wrong host?")
        for fn in usable:
            entry = merged.setdefault(fn["name"], {"fn": fn, "hosts": []})
            entry["hosts"].append(export["host"])
    by_file = {}
    for name in merged:
        other = by_file.setdefault(card_file(name), name)
        if other != name:
            raise GateError(f"'{other}' and '{name}' both map to {card_file(name)}.md")
    return hosts, merged


def merge_constants(exports):
    """Constants merged like functions: first export wins, `hosts` lists every export that
    has it. Only exports that carry a `constants` list count as hosts here, so an export
    taken before constants were exported does not flag every constant as partial."""
    carrying = [e for e in exports if isinstance(e.get("constants"), list)]
    merged = {}
    for export in carrying:
        for const in export["constants"]:
            if not isinstance(const, dict) or not const.get("name") or const.get("exportError"):
                continue
            entry = merged.setdefault(const["name"], {"const": const, "hosts": []})
            entry["hosts"].append(export["host"])
    rows = []
    for name in sorted(merged, key=str.lower):
        const, const_hosts = merged[name]["const"], merged[name]["hosts"]
        rows.append({
            "name": name,
            "type": const.get("type") or "any",
            "value": const.get("value"),
            "summary": constant_summary(const),
            "hosts": const_hosts,
            "partialHosts": len(const_hosts) < len(carrying),
        })
    return rows


def build_rows(ref, hosts, merged):
    notes = stems(os.path.join(ref, "notes"))
    prefixes = library_prefixes(entry["fn"] for entry in merged.values())
    rows = []
    for name in sorted(merged, key=str.lower):
        fn, fn_hosts = merged[name]["fn"], merged[name]["hosts"]
        file = card_file(name)
        category = category_of(fn)
        rows.append({
            "name": name,
            "file": file,
            "kind": kind_of(fn, prefixes),
            "category": category,
            "returns": fn.get("returns") or "any",
            "signature": signature(fn),
            "summary": summary(fn),
            "hosts": fn_hosts,
            "partialHosts": len(fn_hosts) < len(hosts),
            "notes": file in notes,
            "examples": example_count(ref, category, file),
        })
    orphans = sorted(notes - {r["file"] for r in rows})
    if orphans:
        raise GateError("notes without a card: " + ", ".join(f"notes/{o}.md" for o in orphans))
    return rows


def flags(row):
    return ("★" if row["notes"] else "") + ("▶" if row["examples"] else "") + \
           ("⌂" if row["partialHosts"] else "")


def render_card(row, fn, exports_meta):
    source = ", ".join(f"{m['host']} {m.get('hostVersion') or ''}".strip() for m in exports_meta)
    lines = [
        "---",
        f"name: {json.dumps(row['name'])}",
        f"category: {json.dumps(row['category'])}",
        f"returns: {json.dumps(row['returns'])}",
        f"hosts: {json.dumps(row['hosts'])}",
        f"notes: {str(row['notes']).lower()}",
        f"examples: {row['examples']}",
        f"source: {json.dumps('#shared — ' + source)}",
        "---",
        "",
        "<!-- Generated by scripts/sync_shared.py. Do not edit: write in notes/ instead. -->",
        "",
        f"# {row['name']}",
        "",
        "```m",
        row["signature"],
        "```",
        "",
    ]
    description = clean_text(fn.get("longDescription") or fn.get("description"))
    if description:
        lines += [description, ""]
    if row["partialHosts"]:
        lines += [f"> **Not available everywhere.** Present in: {', '.join(row['hosts'])}.", ""]
    params = fn.get("parameters") or []
    if params:
        lines += ["## Parameters", "", "| Name | Type | Optional |", "|---|---|---|"]
        lines += [f"| `{p['name']}` | `{p.get('type') or 'any'}` | "
                  f"{'yes' if p.get('optional') else 'no'} |" for p in params]
        lines.append("")
    if row["notes"]:
        lines += [f"**Field note:** [`notes/{row['file']}.md`](../../notes/{row['file']}.md)", ""]
    if row["examples"]:
        path = f"../../examples/{category_slug(row['category'])}/{row['file']}.md"
        lines += [f"**Executed examples ({row['examples']}):** [{path.lstrip('./')}]({path})", ""]
    examples = [e for e in fn.get("examples") or [] if e.get("code")]
    if examples:
        lines += ["## Examples (engine metadata — not verified here)", ""]
        for e in examples:
            if e.get("description"):
                lines += [clean_text(e["description"]), ""]
            lines += ["```m", e["code"].strip(), "```", ""]
            if e.get("result"):
                lines += ["Stated result:", "", "```m", e["result"].strip(), "```", ""]
    return "\n".join(lines).rstrip() + "\n"


def source_text(exports_meta):
    return ", ".join(f"`{m['host']}` {m.get('hostVersion') or ''}".strip() for m in exports_meta)


CARD_HINT = ("Open one card: `library/<file>.md`, where <file> is the name in lower case with "
             "every run of non-alphanumerics as one dash (`Table.AddColumn` -> `table-addcolumn`).")


def render_catalog_md(rows, exports_meta, n_connectors=0, n_constants=0):
    elsewhere = []
    if n_connectors:
        elsewhere.append(f"{n_connectors} connector entry points are in `connectors.md`")
    if n_constants:
        elsewhere.append(f"{n_constants} constants and type values in `constants.md`")
    lines = [
        "# M function catalogue",
        "",
        f"{len(rows)} library functions from `#shared` ({source_text(exports_meta)}). "
        "Flags: ★ field note · ▶ executed examples · ⌂ not in every host.",
    ]
    if elsewhere:
        lines.append("Not listed here: " + "; ".join(elsewhere) + ".")
    lines += [
        CARD_HINT,
        "",
        "| Function | Category | Returns | Flags | Summary |",
        "|---|---|---|---|---|",
    ]
    lines += [f"| `{r['name']}` | {r['category']} | {r['returns']} | "
              f"{flags(r)} | {r['summary']} |" for r in rows]
    return "\n".join(lines) + "\n"


def render_connectors_md(rows, exports_meta):
    lines = [
        "# M connector entry points",
        "",
        f"{len(rows)} connector functions from `#shared` ({source_text(exports_meta)}): "
        "functions the engine gives no category, from a prefix no library function uses. "
        "Many carry no description. Flags as in `catalog.md`.",
        CARD_HINT,
        "",
        "| Function | Connector | Returns | Flags | Summary |",
        "|---|---|---|---|---|",
    ]
    lines += [f"| `{r['name']}` | {r['category']} | {r['returns']} | "
              f"{flags(r)} | {r['summary']} |" for r in rows]
    return "\n".join(lines) + "\n"


def render_constants_md(rows, exports_meta):
    lines = [
        "# M constants",
        "",
        f"{len(rows)} non-function members of `#shared` ({source_text(exports_meta)}): enum "
        "values, type values and numeric constants. `Value` is the member as text (en-US); "
        "empty when it is not a primitive, such as a type, or when it is a machine setting "
        "such as `Culture.Current`. ⌂ = not in every host. "
        "They have no cards.",
        "",
        "| Name | Type | Value | Flags | Summary |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        value = "" if r["value"] is None else f"`{r['value']}`".replace("|", "\\|")
        lines.append(f"| `{r['name']}` | {r['type']} | {value} | "
                     f"{'⌂' if r['partialHosts'] else ''} | {r['summary']} |")
    return "\n".join(lines) + "\n"


def previous_count(generated):
    path = os.path.join(generated, "catalog.json")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        return len(json.load(f).get("functions", []))


def sync(export_paths, ref=REF, write=False, accept_count_change=False,
         min_functions=MIN_FUNCTIONS):
    exports = [load_export(p) for p in export_paths]
    hosts, merged = merge(exports, min_functions)
    rows = build_rows(ref, hosts, merged)
    library_rows = [r for r in rows if r["kind"] == "library"]
    connector_rows = [r for r in rows if r["kind"] == "connector"]
    constants = merge_constants(exports)
    generated = os.path.join(ref, "generated")

    before = previous_count(generated)
    if before and not accept_count_change:
        drift = abs(len(rows) - before) / before
        if drift > COUNT_TOLERANCE:
            raise GateError(f"function count moved {before} -> {len(rows)} "
                            f"({drift:.0%}). Pass --accept-count-change for a real release.")

    exports_meta = [{"host": e["host"], "hostVersion": e.get("hostVersion") or "",
                     "exportedAt": e.get("exportedAt") or "",
                     "functions": len(e["functions"])} for e in exports]
    report = (f"{len(rows)} functions from {len(exports)} export(s) "
              f"({', '.join(hosts)}): {len(library_rows)} library, "
              f"{len(connector_rows)} connectors; {len(constants)} constants; "
              f"{sum(r['partialHosts'] for r in rows)} functions not in every host, "
              f"{sum(r['notes'] for r in rows)} with notes, "
              f"{sum(1 for r in rows if r['examples'])} with examples.")
    if not write:
        return report

    staging = os.path.join(ref, f".publish-{os.getpid()}")
    shutil.rmtree(staging, ignore_errors=True)
    library = os.path.join(staging, "library")
    os.makedirs(library)
    for row in rows:
        with open(os.path.join(library, f"{row['file']}.md"), "w", encoding="utf-8",
                  newline="\n") as f:
            f.write(render_card(row, merged[row["name"]]["fn"], exports_meta))
    indexes = {
        "catalog.md": render_catalog_md(library_rows, exports_meta,
                                        len(connector_rows), len(constants)),
        "connectors.md": render_connectors_md(connector_rows, exports_meta),
    }
    if constants:
        # Only the exports that carried constants vouch for them.
        constants_meta = [m for m, e in zip(exports_meta, exports)
                          if isinstance(e.get("constants"), list)]
        indexes["constants.md"] = render_constants_md(constants, constants_meta)
    for name, text in indexes.items():
        with open(os.path.join(staging, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    with open(os.path.join(staging, "catalog.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump({"exports": exports_meta, "functions": rows, "constants": constants}, f,
                  ensure_ascii=False, indent=1)
        f.write("\n")

    # Swap in one move, so a failure part-way leaves the previous generated/ as it was.
    retired = os.path.join(ref, f".retired-{os.getpid()}")
    if os.path.isdir(generated):
        os.replace(generated, retired)
    os.replace(staging, generated)
    shutil.rmtree(retired, ignore_errors=True)
    return report + " Written."


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("exports", nargs="+", help="export_shared.pq JSON files, first wins")
    parser.add_argument("--write", action="store_true", help="replace generated/")
    parser.add_argument("--accept-count-change", action="store_true")
    parser.add_argument("--min-functions", type=int, default=MIN_FUNCTIONS)
    args = parser.parse_args(argv)
    try:
        print(sync(args.exports, write=args.write,
                   accept_count_change=args.accept_count_change,
                   min_functions=args.min_functions))
    except GateError as e:
        print(f"SYNC REFUSED: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
