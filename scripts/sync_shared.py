#!/usr/bin/env python3
"""Regenerate plugins/powerquery-m-for-agents/skills/m-reference/generated/ from one or more
#shared exports.

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

Every text a card quotes has a licence. Names, signatures, types, categories and hosts are
facts read from #shared. The one-line descriptions come from Microsoft's MIT-licensed
standard library file (vscode-powerquery, kept as exports/vscode-powerquery-standard-enUs.json;
THIRD_PARTY_NOTICES.md at the plugin root); a function or constant that file does not describe
gets no description. The engine's own long descriptions and examples, which carry no stated
licence, are not copied (#1). A card links its Microsoft Learn page when
exports/learn-links.json, written by lab/shared-export/learn_links.py, says the page exists.

The non-function members of #shared (GroupKind.Local, JoinKind.Inner, Int64.Type, ...)
go to constants.md, merged across hosts the same way. They have no cards: one row says it
all. An export taken before the query exported constants simply contributes none.

Everything under generated/ is replaced wholesale. notes/ and examples/ are read to set
the ★ and ▶ flags and are never written.

The cards are packed: generated/library/<part>.md holds every card of one catalogue part, one
`## <Name>` section each, because the plugin directory holds a plugin of more than 512 files
for review. A part that would pass CARD_FILE_LIMIT continues in <part>-2.md; each index row
names the file its card is in. The executed examples are packed the same way, by hand:
examples/<category>.md, one `## <Name>` section per function (sections() reads both).

Gates, all checked before anything is written:
  - an export with fewer than --min-functions functions (wrong query, wrong host);
  - two functions that map to the same card filename;
  - a notes/<file>.md with no card;
  - the function count moving more than 5% from the last catalogue, unless
    --accept-count-change.

The catalogue for scripts is catalog/ at the repository root, outside the shipped plugin: one
JSON file per category root, plus connectors.json, constants.json and index.json.
load_catalog() reads it back whole.

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

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(REPO, "plugins", "powerquery-m-for-agents", "skills", "m-reference")
CATALOG = os.path.join(REPO, "catalog")
CARD_FILE_LIMIT = 256 * 1024
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


def summary(description):
    text = re.sub(r"\s+", " ", clean_text(description))
    return truncate(re.split(r"(?<=\.)\s", text, maxsplit=1)[0], SUMMARY_CHARS)


def constant_summary(description):
    return truncate(re.sub(r"\s+", " ", clean_text(description)), CONSTANT_SUMMARY_CHARS)


DESCRIPTIONS = os.path.join(REPO, "exports", "vscode-powerquery-standard-enUs.json")
LEARN_LINKS = os.path.join(REPO, "exports", "learn-links.json")
NOTICE = "THIRD_PARTY_NOTICES.md"


def load_descriptions(path):
    """{name: description} from Microsoft's standard library file (MIT). Empty when the file
    is absent: then nothing is described, rather than something described without a licence."""
    if not path or not os.path.isfile(path):
        return {}
    with open(path, encoding="utf-8-sig") as f:
        entries = json.load(f)
    out = {}
    for entry in entries:
        text = ((entry.get("documentation") or {}).get("description") or "").strip()
        if entry.get("name") and text:
            out[entry["name"]] = text
    return out


def load_learn_links(path):
    """(base URL, {card file}) for the functions whose Microsoft Learn page was checked."""
    if not path or not os.path.isfile(path):
        return "", set()
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("base", ""), set(data.get("files", []))


def stems(directory):
    if not os.path.isdir(directory):
        return set()
    return {os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith(".md")}


def sections(text):
    """[(name, body)] for every `## <name>` heading of a packed page, outside code fences, in
    order. A ```m block may hold a line starting with #, never a heading."""
    out, name, body, fence = [], None, [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            fence = not fence
        if not fence and line.startswith("## "):
            if name is not None:
                out.append((name, "\n".join(body)))
            name, body = line[3:].strip(), []
        elif name is not None:
            body.append(line)
    if name is not None:
        out.append((name, "\n".join(body)))
    return out


def example_counts(ref):
    """{(category slug, function name): number of ```m blocks} from examples/<category>.md."""
    folder = os.path.join(ref, "examples")
    counts = {}
    for slug in sorted(stems(folder)):
        with open(os.path.join(folder, f"{slug}.md"), encoding="utf-8") as f:
            for name, body in sections(f.read()):
                counts[(slug, name)] = len(re.findall(r"^```m\s*$", body, re.M))
    return counts


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


def merge_constants(exports, descriptions=None):
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
            "summary": constant_summary((descriptions or {}).get(name)),
            "hosts": const_hosts,
            "partialHosts": len(const_hosts) < len(carrying),
        })
    return rows


def build_rows(ref, hosts, merged, descriptions=None):
    notes = stems(os.path.join(ref, "notes"))
    examples = example_counts(ref)
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
            "summary": summary((descriptions or {}).get(name)),
            "hosts": fn_hosts,
            "partialHosts": len(fn_hosts) < len(hosts),
            "notes": file in notes,
            "examples": examples.get((category_slug(category), name), 0),
        })
    orphans = sorted(notes - {r["file"] for r in rows})
    if orphans:
        raise GateError("notes without a card: " + ", ".join(f"notes/{o}.md" for o in orphans))
    return rows


def flags(row):
    return ("★" if row["notes"] else "") + ("▶" if row["examples"] else "") + \
           ("⌂" if row["partialHosts"] else "")


def render_section(row, fn, description="", learn_url=""):
    """One card as a `## <Name>` section of its packed library file."""
    lines = [
        f"## {row['name']}",
        "",
        "```m",
        row["signature"],
        "```",
        "",
        f"Category: {row['category']} · hosts: {', '.join(row['hosts'])}",
        "",
    ]
    description = clean_text(description)
    if description:
        lines += [description, "",
                  f"*Description: Microsoft, MIT ([{NOTICE}](../../../../{NOTICE})).*", ""]
    if learn_url:
        lines += [f"Reference: [Microsoft Learn]({learn_url})", ""]
    if row["partialHosts"]:
        lines += [f"> **Not available everywhere.** Present in: {', '.join(row['hosts'])}.", ""]
    params = fn.get("parameters") or []
    if params:
        lines += ["### Parameters", "", "| Name | Type | Optional |", "|---|---|---|"]
        lines += [f"| `{p['name']}` | `{p.get('type') or 'any'}` | "
                  f"{'yes' if p.get('optional') else 'no'} |" for p in params]
        lines.append("")
    if row["notes"]:
        lines += [f"**Field note:** [`notes/{row['file']}.md`](../../notes/{row['file']}.md)", ""]
    if row["examples"]:
        path = f"../../examples/{category_slug(row['category'])}.md"
        lines += [f"**Executed examples ({row['examples']}):** [{path.lstrip('./')}]({path}), "
                  f"section `## {row['name']}`", ""]
    return "\n".join(lines).rstrip() + "\n"


def library_header(card, count, exports_meta):
    return "\n".join([
        f"# M library cards: {card}",
        "",
        "<!-- Generated by scripts/sync_shared.py. Do not edit: write in notes/ instead. -->",
        "",
        f"{count} cards from `#shared` ({source_text(exports_meta)}), one `## <Name>` section "
        "each. Find the line `## <Name>` and read to the next `## `; do not read the file whole.",
        "",
    ]) + "\n"


def pack_cards(rows, sections_by_name, exports_meta, limit=CARD_FILE_LIMIT):
    """{card file stem: text}, one file per catalogue part, a part continuing in <part>-2,
    <part>-3... when the next card would take it past `limit` bytes. Sets row["card"]."""
    files, order = {}, {}
    for row in rows:
        order.setdefault(catalog_part(row), []).append(row)
    for part, part_rows in order.items():
        chunks, current, size = [], [], 0
        for row in part_rows:
            weight = len(sections_by_name[row["name"]].encode("utf-8")) + 1
            if current and size + weight > limit - 1024:
                chunks.append(current)
                current, size = [], 0
            current.append(row)
            size += weight
        chunks.append(current)
        for i, chunk in enumerate(chunks):
            card = part if i == 0 else f"{part}-{i + 1}"
            for row in chunk:
                row["card"] = card
            files[card] = library_header(card, len(chunk), exports_meta) + "\n".join(
                sections_by_name[r["name"]] for r in chunk)
    return files


def source_text(exports_meta):
    return ", ".join(f"`{m['host']}` {m.get('hostVersion') or ''}".strip() for m in exports_meta)


CARD_HINT = ("A card is a section of `library/<Card>.md`: search that file for the line "
             "`## <Function>` and read from there to the next `## `.")


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
        "Flags: ★ field note · ▶ executed examples · ⌂ not in every host. "
        f"Summaries: Microsoft, MIT (`{NOTICE}`); empty where Microsoft's file has none.",
    ]
    if elsewhere:
        lines.append("Not listed here: " + "; ".join(elsewhere) + ".")
    lines += [
        CARD_HINT,
        "",
        "| Function | Category | Returns | Flags | Card | Summary |",
        "|---|---|---|---|---|---|",
    ]
    lines += [f"| `{r['name']}` | {r['category']} | {r['returns']} | "
              f"{flags(r)} | {r['card']} | {r['summary']} |" for r in rows]
    return "\n".join(lines) + "\n"


def render_connectors_md(rows, exports_meta):
    lines = [
        "# M connector entry points",
        "",
        f"{len(rows)} connector functions from `#shared` ({source_text(exports_meta)}): "
        "functions the engine gives no category, from a prefix no library function uses. "
        "No licensed description exists for them, so none is given. Flags as in `catalog.md`.",
        CARD_HINT,
        "",
        "| Function | Connector | Returns | Flags | Card |",
        "|---|---|---|---|---|",
    ]
    lines += [f"| `{r['name']}` | {r['category']} | {r['returns']} | {flags(r)} | {r['card']} |"
              for r in rows]
    return "\n".join(lines) + "\n"


def render_constants_md(rows, exports_meta):
    lines = [
        "# M constants",
        "",
        f"{len(rows)} non-function members of `#shared` ({source_text(exports_meta)}): enum "
        "values, type values and numeric constants. `Value` is the member as text (en-US); "
        "empty when it is not a primitive, such as a type, or when it is a machine setting "
        "such as `Culture.Current`. ⌂ = not in every host. "
        f"They have no cards. Summaries: Microsoft, MIT (`{NOTICE}`).",
        "",
        "| Name | Type | Value | Flags | Summary |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        value = "" if r["value"] is None else f"`{r['value']}`".replace("|", "\\|")
        lines.append(f"| `{r['name']}` | {r['type']} | {value} | "
                     f"{'⌂' if r['partialHosts'] else ''} | {r['summary']} |")
    return "\n".join(lines) + "\n"


RESERVED_PARTS = {"index", "connectors", "constants"}


def catalog_part(row):
    """The file a row goes in: connectors together, library functions by category root."""
    if row.get("kind") == "connector":
        return "connectors"
    return category_slug((row.get("category") or "").split(".")[0])


def write_catalog(folder, exports_meta, rows, constants):
    """Write the catalogue folder: index.json (the exports and the part files), one file per
    part, and constants.json. load_catalog reads it back as one dict."""
    parts = {}
    for row in rows:
        parts.setdefault(catalog_part(row), []).append(row)
    clash = sorted(p for p in parts if p in RESERVED_PARTS and p != "connectors")
    if clash or any(r.get("kind") != "connector" for r in parts.get("connectors", [])):
        raise GateError("a category root takes a reserved catalogue file name: "
                        f"{clash or ['connectors']}")
    os.makedirs(folder, exist_ok=True)

    def dump(name, value):
        with open(os.path.join(folder, name + ".json"), "w", encoding="utf-8", newline="\n") as f:
            json.dump(value, f, ensure_ascii=False, indent=1)
            f.write("\n")

    for name, part in parts.items():
        dump(name, {"functions": part})
    dump("constants", {"constants": constants})
    dump("index", {"exports": exports_meta, "parts": sorted(parts)})


def load_catalog(folder=CATALOG):
    """The catalogue folder as one dict, {exports, functions, constants}, the functions in the
    order the sync wrote them (by name, case-insensitive). None when there is no catalogue."""
    index_path = os.path.join(folder, "index.json")
    if not os.path.isfile(index_path):
        return None
    with open(index_path, encoding="utf-8") as f:
        index = json.load(f)
    functions = []
    for name in index.get("parts", []):
        with open(os.path.join(folder, name + ".json"), encoding="utf-8") as f:
            functions.extend(json.load(f)["functions"])
    constants = []
    path = os.path.join(folder, "constants.json")
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            constants = json.load(f)["constants"]
    functions.sort(key=lambda r: r["name"].lower())
    return {"exports": index.get("exports", []), "functions": functions, "constants": constants}


def previous_count(catalog_dir):
    catalog = load_catalog(catalog_dir)
    return None if catalog is None else len(catalog.get("functions", []))


def sync(export_paths, ref=REF, write=False, accept_count_change=False,
         min_functions=MIN_FUNCTIONS, descriptions=None, learn=("", frozenset()),
         catalog_dir=CATALOG):
    exports = [load_export(p) for p in export_paths]
    hosts, merged = merge(exports, min_functions)
    descriptions = descriptions or {}
    learn_base, learn_files = learn
    rows = build_rows(ref, hosts, merged, descriptions)
    library_rows = [r for r in rows if r["kind"] == "library"]
    connector_rows = [r for r in rows if r["kind"] == "connector"]
    constants = merge_constants(exports, descriptions)
    generated = os.path.join(ref, "generated")

    before = previous_count(catalog_dir)
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
    sections_by_name = {
        row["name"]: render_section(row, merged[row["name"]]["fn"],
                                    descriptions.get(row["name"], ""),
                                    learn_base + row["file"] if row["file"] in learn_files else "")
        for row in rows}
    for card, text in pack_cards(rows, sections_by_name, exports_meta).items():
        with open(os.path.join(library, f"{card}.md"), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
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
    catalog_staging = os.path.join(staging, "catalog")
    write_catalog(catalog_staging, exports_meta, rows, constants)

    # Swap in one move each, so a failure part-way leaves the previous output as it was.
    catalog_new = catalog_dir.rstrip("\\/") + f".publish-{os.getpid()}"
    shutil.rmtree(catalog_new, ignore_errors=True)
    shutil.move(catalog_staging, catalog_new)
    for new, target in ((staging, generated), (catalog_new, catalog_dir)):
        retired = target.rstrip("\\/") + f".retired-{os.getpid()}"
        if os.path.isdir(target):
            os.replace(target, retired)
        os.replace(new, target)
        shutil.rmtree(retired, ignore_errors=True)
    return report + " Written."


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("exports", nargs="+", help="export_shared.pq JSON files, first wins")
    parser.add_argument("--write", action="store_true", help="replace generated/")
    parser.add_argument("--accept-count-change", action="store_true")
    parser.add_argument("--min-functions", type=int, default=MIN_FUNCTIONS)
    parser.add_argument("--descriptions", default=DESCRIPTIONS,
                        help="Microsoft's MIT standard library file (vscode-powerquery)")
    parser.add_argument("--learn-links", default=LEARN_LINKS,
                        help="the Learn pages checked by lab/shared-export/learn_links.py")
    args = parser.parse_args(argv)
    try:
        print(sync(args.exports, write=args.write,
                   accept_count_change=args.accept_count_change,
                   min_functions=args.min_functions,
                   descriptions=load_descriptions(args.descriptions),
                   learn=load_learn_links(args.learn_links)))
    except GateError as e:
        print(f"SYNC REFUSED: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
