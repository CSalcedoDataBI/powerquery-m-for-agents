#!/usr/bin/env python3
"""Check the executed examples without running them (CI has no Power BI Desktop).

  1. Every ```m block in a hand-written page under skills/ is followed by its ```text result,
     and a page with blocks carries the lab stamp (`<!-- lab: desktop <build> -->`). The
     results themselves are written by lab/runner/run_examples.py, on a machine with Desktop.
  2. examples/<category>/<file>.md belongs to a card, under that card's category - the path
     sync_shared.py looks at to set the ▶ flag. Anywhere else the example is never linked.
  3. No invented names: every `Prefix.Name` in a page is a function or constant the export
     has, or a name the engine itself printed in some result (an error reason such as
     `Expression.Error`, a metadata field such as `Documentation.Name`).

  python scripts/check_examples.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import m_blocks  # noqa: E402

REF = os.path.join(m_blocks.SKILLS, "m-reference")
# Most library names are Prefix.Name (Table.AddColumn, Int64.Type): any such token is checked.
NAME_RE = re.compile(r"(?<![\w.])([A-Z][A-Za-z0-9]*\.[A-Z][A-Za-z0-9]*)(?![\w])")
# Some are not (appFigures.Tables, BinaryFormat.7BitEncodedSignedInteger). A looser token is
# checked only when its prefix is one the export uses, so `catalog.md` or `e.g` never count.
LOOSE_RE = re.compile(r"(?<![\w.])([A-Za-z][A-Za-z0-9]*\.[A-Za-z0-9][A-Za-z0-9]*)(?![\w])")
# Names the engine prints that are not library members: error reasons in `error: <Reason>:`.
REASON_RE = re.compile(r"error: ([A-Za-z][A-Za-z0-9]*\.[A-Za-z][A-Za-z0-9]*):")


STRING_RE = re.compile(r'"(?:[^"]|"")*"')


def names_in(text, prefixes):
    found = set(NAME_RE.findall(text))
    found |= {n for n in LOOSE_RE.findall(text) if n.split(".", 1)[0] in prefixes}
    return found


def code_names(code):
    """Every a.b token in M code outside text literals. M has no other use for a dot between
    identifiers, so each one is a library name - including a misspelled lowercase prefix,
    which the prose check cannot tell from a file name."""
    return set(LOOSE_RE.findall(STRING_RE.sub('""', code)))


def category_slug(category):
    return re.sub(r"[^a-z0-9]+", "-", category.lower()).strip("-") or "uncategorised"


def load_catalog(ref):
    path = os.path.join(ref, "generated", "catalog.json")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def check(root=m_blocks.ROOT, ref=REF, page_list=None):
    errors = []
    pages = page_list if page_list is not None else m_blocks.pages()
    texts = {}
    for page in pages:
        with open(os.path.join(root, page), encoding="utf-8") as f:
            texts[page] = f.read()

    # 1: results and stamps
    parsed, results = {}, []
    for page, text in texts.items():
        try:
            blocks = m_blocks.find_blocks(text)
        except ValueError as e:
            errors.append(f"{page}: {e}")
            continue
        parsed[page] = blocks
        for i, block in enumerate(blocks):
            if block.result is None:
                errors.append(f"{page}: ```m block {i + 1} (line {block.code_start + 1}) has no "
                              "```text result - run lab/runner/run_examples.py --write")
            else:
                results.append(block.result)
        if blocks and not m_blocks.stamp(text):
            errors.append(f"{page}: has ```m blocks but no '<!-- lab: <host> <build> -->' stamp")

    catalog = load_catalog(ref)
    if catalog is None:
        return errors
    functions = {r["name"]: r for r in catalog.get("functions", [])}
    exported = set(functions) | {c["name"] for c in catalog.get("constants", [])}
    prefixes = {n.split(".", 1)[0] for n in exported}
    # What the engine printed vouches for names the code never wrote: error reasons
    # (Expression.Error), metadata fields (Documentation.Name). A name that also appears in
    # some ```m block cannot be vouched for this way - an error message, or a `try` record's
    # Message, repeats the very name that failed ("The name 'Text.Uppercase' ...").
    written = set()
    for blocks in parsed.values():
        for block in blocks:
            written |= code_names(block.code)
    printed = set()
    for result in results:
        printed |= set(REASON_RE.findall(result)) | names_in(result, prefixes)
    known = exported | (printed - written)

    # 2: example placement
    by_file = {r["file"]: r for r in functions.values()}
    examples_root = os.path.relpath(os.path.join(ref, "examples"), root).replace("\\", "/") + "/"
    for page in texts:
        if not page.startswith(examples_root):
            continue
        parts = page[len(examples_root):].split("/")
        if len(parts) != 2:
            errors.append(f"{page}: examples go in examples/<category>/<file>.md")
            continue
        folder, file = parts[0], parts[1][:-3]
        row = by_file.get(file)
        if row is None:
            errors.append(f"{page}: no card generated/library/{file}.md")
        elif category_slug(row["category"]) != folder:
            errors.append(f"{page}: {row['name']} is in category '{row['category']}', so its "
                          f"examples go in examples/{category_slug(row['category'])}/")

    # 3: no invented names, outside the engine's own result blocks
    for page, blocks in parsed.items():
        prose = texts[page]
        for block in reversed(blocks):
            if block.result is not None:
                lines = prose.split("\n")
                prose = "\n".join(lines[:block.result_start] + lines[block.result_end + 1:])
        in_code = set().union(*(code_names(b.code) for b in blocks)) if blocks else set()
        for name in sorted((names_in(prose, prefixes) | in_code) - known):
            errors.append(f"{page}: '{name}' is not in the export nor printed by the engine")
    return errors


def main():
    errors = check()
    if errors:
        print("EXAMPLES CHECK FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1
    n_pages = sum(1 for p in m_blocks.pages()
                  if m_blocks.find_blocks(open(os.path.join(m_blocks.ROOT, p), encoding="utf-8").read()))
    print(f"OK: executed examples consistent ({n_pages} page(s) with ```m blocks).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
