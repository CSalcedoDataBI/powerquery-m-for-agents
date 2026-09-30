#!/usr/bin/env python3
"""Build one review PBIP per example category, to read the examples in Power BI.

  python lab/review/build_review.py --only number-  # build the batches whose folder matches
  python lab/review/build_review.py                 # rebuild every batch already in lab/review/
  python lab/review/build_review.py --check         # exit 1 if a committed batch is out of date

A batch is added with --only; after that it is rebuilt with the rest, and CI checks it.

The example pages under skills/m-reference/examples/<category>/ stay the source of truth: this
only turns them into a Power BI project. Open it, Refresh, and the first page lists every
block with the result its page records, the result the engine returns now, and whether they
match. The last page is the author's "Thank You!!" page (lab/review/thank-you/).

Refresh evaluates each block the way lab/runner does: runner.pq renders the value, over only
the members of #shared that m_blocks.allowed_names allows. Blocks are the checked pages of this
repository (check_examples.py refuses any that could reach outside the engine).
"""
import argparse
import json
import os
import re
import shutil
import sys
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "lab", "shared-export"))

import m_blocks  # noqa: E402
from build_pbip import json_text, project_files, tmdl_source  # noqa: E402
from check_examples import category_slug  # noqa: E402

EXAMPLES = os.path.join(ROOT, "skills", "m-reference", "examples")
CATALOG = os.path.join(ROOT, "skills", "m-reference", "generated", "catalog.json")
RUNNER = os.path.join(ROOT, "lab", "runner", "runner.pq")
THANK_YOU = os.path.join(HERE, "thank-you")
GENERATOR = "lab/review/build_review.py from the example pages"
COLUMNS = [("seq", "int64"), ("Function", "string"), ("Block", "int64"), ("Code", "string"),
           ("Recorded", "string"), ("Live", "string"), ("Match", "string")]
DENEB = "deneb7E15AEF80B9E4D4F8E12924291ECE89A"
SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition"


def m_text(value):
    v = value.replace("#(", "#(#)(").replace('"', '""')
    v = v.replace("\r", "#(cr)").replace("\n", "#(lf)").replace("\t", "#(tab)")
    return f'"{v}"'


def guid(*parts):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, "powerquery-m-for-agents/review/" + "/".join(parts)))


def project_name(category):
    """Number.Conversion and formatting -> NumberConversionAndFormatting."""
    return "".join(w[:1].upper() + w[1:] for w in re.split(r"[^A-Za-z0-9]+", category) if w)


def categories(catalog, only=""):
    """{category: [(function, page path, [blocks])]} for every examples/<folder>/ with pages."""
    by_file = {r["file"]: r for r in catalog["functions"]}
    found = {}
    for folder in sorted(os.listdir(EXAMPLES)):
        if only and not any(o in folder for o in only.split(",")):
            continue
        path = os.path.join(EXAMPLES, folder)
        if not os.path.isdir(path):
            continue
        for name in sorted(os.listdir(path)):
            row = by_file.get(name[:-3])
            if not name.endswith(".md") or row is None:
                continue
            with open(os.path.join(path, name), encoding="utf-8") as f:
                blocks = m_blocks.find_blocks(f.read())
            if blocks:
                found.setdefault(row["category"], []).append((row["name"], blocks))
    return found


def partition(rows, allowed):
    """The model's query: the examples as a table, each block rendered live by runner.pq."""
    with open(RUNNER, encoding="utf-8") as f:
        runner = f.read()
    cases = ", ".join("{" + m_text(str(i)) + ", " + m_text(code) + "}"
                      for i, (_, _, code, _) in enumerate(rows))
    runner = runner.replace("    Cases = {},", "    Cases = {" + cases + "},", 1)
    runner = runner.replace("    Allowed = {},", "    Allowed = {" + ", ".join(m_text(n) for n in allowed) + "},", 1)
    listed = ", ".join("{" + ", ".join([str(i), m_text(fn), str(b + 1), m_text(code), m_text(rec or "")]) + "}"
                       for i, (fn, b, code, rec) in enumerate(rows))
    return (
        "let\n"
        "    Live = \n" + "\n".join("        " + line for line in runner.splitlines()) + ",\n"
        "    Pages = #table(type table [seq = Int64.Type, Function = text, Block = Int64.Type, "
        "Code = text, Recorded = text], {" + listed + "}),\n"
        "    Joined = Table.NestedJoin(Pages, \"seq\", Table.TransformColumns(Live, {{\"id\", Number.From}}), "
        "\"id\", \"L\", JoinKind.LeftOuter),\n"
        "    Expanded = Table.ExpandTableColumn(Joined, \"L\", {\"result\"}, {\"Live\"}),\n"
        "    Matched = Table.AddColumn(Expanded, \"Match\", each if [Live] = [Recorded] then \"yes\" "
        "else \"NO\", type text),\n"
        "    Sorted = Table.Sort(Matched, {{\"seq\", Order.Ascending}})\n"
        "in\n"
        "    Sorted")


def field(table, column):
    return {"field": {"Column": {"Expression": {"SourceRef": {"Entity": table}}, "Property": column}},
            "queryRef": f"{table}.{column}", "nativeQueryRef": column}


def measure(table, name):
    return {"field": {"Measure": {"Expression": {"SourceRef": {"Entity": table}}, "Property": name}},
            "queryRef": f"{table}.{name}", "nativeQueryRef": name}


def literal(value):
    return {"expr": {"Literal": {"Value": value}}}


def examples_page(name, category, count):
    visuals = {
        "title": {"visualType": "textbox", "position": {"x": 24, "y": 12, "z": 0, "width": 1232, "height": 56},
                  "objects": {"general": [{"properties": {"paragraphs": [{"textRuns": [
                      {"value": f"{category} - {count} examples. Refresh to run them in this Power BI.",
                       "textStyle": {"fontSize": "18pt", "fontWeight": "bold"}}]}]}}]}},
        "slicer": {"visualType": "slicer", "position": {"x": 24, "y": 80, "z": 1, "width": 260, "height": 620},
                   "query": {"queryState": {"Values": {"projections": [field(name, "Function")]}}},
                   "objects": {"data": [{"properties": {"mode": literal("'Basic'")}}]}},
        "table": {"visualType": "tableEx", "position": {"x": 300, "y": 80, "z": 2, "width": 956, "height": 620},
                  "query": {"queryState": {"Values": {"projections": [
                      field(name, c) for c in ("Function", "Block", "Code", "Recorded", "Live", "Match")]}}}},
    }
    files = {}
    for vid, v in visuals.items():
        body = {"$schema": f"{SCHEMA}/visualContainer/2.12.0/schema.json", "name": vid,
                "position": v["position"], "visual": {k: v[k] for k in ("visualType", "query", "objects") if k in v}}
        files[f"definition/pages/examples/visuals/{vid}/visual.json"] = json_text(body)
    files["definition/pages/examples/page.json"] = json_text({
        "$schema": f"{SCHEMA}/page/2.1.0/schema.json", "name": "examples", "displayName": "Examples",
        "displayOption": "FitToPage", "height": 720, "width": 1280})
    return files


def thank_you_page(name):
    """The author's page, with its Deneb cover bound to this model (its spec draws fixed links
    and reads no data, but Deneb needs fields to render)."""
    files = {}
    with open(os.path.join(THANK_YOU, "page.json"), encoding="utf-8") as f:
        page = json.load(f)
    page["name"] = "thankyou"
    files["definition/pages/thankyou/page.json"] = json_text(page)
    visuals = os.path.join(THANK_YOU, "visuals")
    for vid in sorted(os.listdir(visuals)):
        with open(os.path.join(visuals, vid, "visual.json"), encoding="utf-8") as f:
            v = json.load(f)
        if v["visual"]["visualType"] == DENEB:
            v["visual"]["query"] = {"queryState": {"dataset": {"projections": [
                field(name, "Function"), measure(name, "Examples")]}}}
            # The source page filters on its own model's fields; here they do not exist.
            v.pop("filterConfig", None)
        files[f"definition/pages/thankyou/visuals/{vid}/visual.json"] = json_text(v)
    return files


def project(category, functions, allowed):
    name = project_name(category)
    rows = [(fn, b, block.code, block.result) for fn, blocks in functions for b, block in enumerate(blocks)]
    ids = {"generator": GENERATOR, "model": guid(name, "model"), "report": guid(name, "report"),
           "table": guid(name, "table"), "columns": [guid(name, c) for c, _ in COLUMNS]}
    files = project_files(name, tmdl_source(partition(rows, allowed)), COLUMNS, ids)
    table = f"{name}.SemanticModel/definition/tables/{name}.tmdl"
    files[table] = files[table].replace(
        "\tpartition ",
        f"\tmeasure Examples = COUNTROWS('{name}')\n"
        "\t\tformatString: 0\n"
        f"\t\tlineageTag: {guid(name, 'measure')}\n\n"
        "\tpartition ", 1)
    rp = f"{name}.Report/"
    del files[rp + "definition/pages/export/page.json"]
    report = json.loads(files[rp + "definition/report.json"])
    report["publicCustomVisuals"] = [DENEB]
    files[rp + "definition/report.json"] = json_text(report)
    files[rp + "definition/pages/pages.json"] = json_text({
        "$schema": f"{SCHEMA}/pagesMetadata/1.0.0/schema.json",
        "pageOrder": ["examples", "thankyou"], "activePageName": "examples"})
    for rel, text in {**examples_page(name, category, len(rows)), **thank_you_page(name)}.items():
        files[rp + rel] = text
    return category_slug(category), files


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--only", default="")
    args = parser.parse_args(argv)
    with open(CATALOG, encoding="utf-8") as f:
        catalog = json.load(f)
    allowed = m_blocks.allowed_names(catalog)
    stale = []
    for category, functions in categories(catalog, args.only).items():
        slug, files = project(category, functions, allowed)
        folder = os.path.join(HERE, slug)
        if not args.only and not os.path.isdir(folder):
            continue
        on_disk = {}
        if os.path.isdir(folder):
            for dirpath, _, names in os.walk(folder):
                for n in names:
                    p = os.path.join(dirpath, n)
                    on_disk[os.path.relpath(p, folder).replace("\\", "/")] = open(p, encoding="utf-8").read()
        if args.check:
            if on_disk != files:
                stale.append(slug)
            continue
        if on_disk != files:
            shutil.rmtree(folder, ignore_errors=True)
            for rel, text in files.items():
                path = os.path.join(folder, rel)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(text)
            print(f"wrote {slug}/{project_name(category)}.pbip ({len(functions)} functions)")
    if stale:
        print("Out of date: " + ", ".join(stale) + " - run python lab/review/build_review.py")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
