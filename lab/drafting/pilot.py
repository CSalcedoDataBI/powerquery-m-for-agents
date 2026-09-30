#!/usr/bin/env python3
"""Draft executed-example pages with an outside model, and take back only what is safe.

  python lab/drafting/pilot.py prompts --out lab/drafting/out/dsh     # one prompt per function
  (run_dsh.ps1 answers each prompt in a container)
  python lab/drafting/pilot.py collect --out lab/drafting/out/dsh     # answers -> examples/
  python lab/drafting/pilot.py report  --out lab/drafting/out/dsh     # the measurements

The model writes only the ```m blocks and the note. Nothing it writes is trusted:

  - Any ```text block or lab stamp in an answer is dropped. Results come from
    lab/runner/run_examples.py, never from the model.
  - A block that could reach outside the engine (m_blocks.unsafe_calls) keeps the whole page
    out: the runner would evaluate it on this machine.
  - Outside ```m blocks a page may hold headings and plain prose only: another fence, HTML,
    an image or a link refuses it (off_format).
  - A page is written only under examples/<category>/<file>.md of a pilot function, and never
    over an existing page unless --force says so.

Issue #21 has the pilot scope and the isolation rules.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import m_blocks  # noqa: E402
from check_examples import category_slug  # noqa: E402

REF = os.path.join(ROOT, "skills", "m-reference")
PILOT_CATEGORIES = ["Number.Operations", "Number.Conversion and formatting"]
# The format the model copies: one page with a single block, one with two.
MODELS = ["examples/list-information/list-count.md",
          "examples/table-transformation/table-fuzzyjoin.md"]

INSTRUCTIONS = """\
You write one example page for a Power Query M reference library.

Write the page for {name}. Its reference card follows, then two pages in the exact format.

Rules:
- Start with "# {name}", then one short sentence saying what the examples show.
- Then one to three ```m blocks. Each block is one M expression on literal values.
- Show behaviour a reader could get wrong: nulls, optional arguments, edge cases.
- Use only {name} and simple library functions (Number.*, Text.*, List.*, Record.*).
- No data sources: no files, no web, no databases, no #shared.
- Do NOT write results, ```text blocks or the "<!-- lab: ... -->" line. The blocks are
  run in the real engine afterwards and the results written from that run.
- Answer with the page only: no preamble, no explanation, no tool calls.

=== Reference card for {name} ===
{card}
=== Format example 1 ===
{model1}
=== Format example 2 ===
{model2}
"""


def load_catalog():
    with open(os.path.join(REF, "generated", "catalog.json"), encoding="utf-8") as f:
        return json.load(f)


def pilot_rows(catalog):
    rows = [r for r in catalog["functions"]
            if r.get("kind") == "library" and r.get("category") in PILOT_CATEGORIES]
    return sorted(rows, key=lambda r: r["name"])


def strip_results(text):
    """The page without any ```text block or stamp line, and how many blocks were dropped."""
    lines, out, dropped, i = text.split("\n"), [], 0, 0
    while i < len(lines):
        if lines[i].rstrip() == "```text":
            j = i + 1
            while j < len(lines) and lines[j].rstrip() != "```":
                j += 1
            dropped += 1
            i = j + 1
            continue
        if not m_blocks.STAMP_RE.match(lines[i]):
            out.append(lines[i])
        i += 1
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n", dropped


def unwrap(text):
    """Models often wrap the whole answer in ```markdown ... ```."""
    t = text.strip()
    m = re.fullmatch(r"```(?:markdown|md)?\n(.*)\n```", t, re.S)
    return m.group(1) if m else t


FENCE_RE = re.compile(r"^```(\w*)\s*$")


def off_format(page):
    """Why a page is not in the example format, or None. Beyond ```m blocks the model may
    write headings and plain prose - no other fence, HTML, image or link: nothing it writes
    is reviewed as code, so nothing it writes may act as more than text."""
    in_block = False
    for line in page.splitlines():
        m = FENCE_RE.match(line)
        if m:
            if not in_block and m.group(1) != "m":
                return f"a ```{m.group(1)} fence"
            in_block = not in_block
            continue
        if in_block:
            continue
        if re.search(r"<[A-Za-z!/]", line):
            return "HTML"
        if re.search(r"\]\(|https?://|www\.", line):
            return "a link"
    return None


def cmd_prompts(args):
    catalog = load_catalog()
    models = []
    for rel in MODELS:
        with open(os.path.join(REF, rel), encoding="utf-8") as f:
            models.append(strip_results(f.read())[0])
    folder = os.path.join(args.out, "prompts")
    os.makedirs(folder, exist_ok=True)
    rows = pilot_rows(catalog)
    for r in rows:
        with open(os.path.join(REF, "generated", "library", r["file"] + ".md"), encoding="utf-8") as f:
            card = f.read()
        text = INSTRUCTIONS.format(name=r["name"], card=card, model1=models[0], model2=models[1])
        with open(os.path.join(folder, r["file"] + ".txt"), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    print(f"Wrote {len(rows)} prompt(s) to {folder}")
    return 0


def final_text(path):
    """The answer of one run: the `final` event of dsh --json, or the file itself."""
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    if not path.endswith(".jsonl"):
        return raw
    final = None
    for line in raw.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get("type") == "final":
            final = event.get("text") or ""
    return final


def cmd_collect(args):
    catalog = load_catalog()
    by_file = {r["file"]: r for r in pilot_rows(catalog)}
    answers = os.path.join(args.out, "answers")
    results = {}
    for name in sorted(os.listdir(answers)) if os.path.isdir(answers) else []:
        file, ext = os.path.splitext(name)
        if ext not in (".md", ".jsonl") or file not in by_file:
            continue
        row = by_file[file]
        entry = results.setdefault(row["name"], {})
        text = final_text(os.path.join(answers, name))
        if not text:
            entry["status"] = "no answer"
            continue
        page, dropped = strip_results(unwrap(text))
        entry["results_dropped"] = dropped
        try:
            blocks = m_blocks.find_blocks(page)
        except ValueError as e:
            entry["status"] = f"unreadable: {e}"
            continue
        entry["blocks"] = len(blocks)
        unsafe = sorted({n for b in blocks for n in m_blocks.unsafe_calls(b.code, catalog)})
        if unsafe:
            entry["status"] = "refused: " + ", ".join(unsafe)
            continue
        if not blocks:
            entry["status"] = "no ```m block"
            continue
        why = off_format(page)
        if why:
            entry["status"] = f"refused: {why}"
            continue
        if not page.startswith(f"# {row['name']}\n"):
            page = f"# {row['name']}\n\n" + page
        rel = f"examples/{category_slug(row['category'])}/{file}.md"
        target = os.path.join(REF, rel)
        if os.path.exists(target) and not args.force:
            entry["status"] = "exists (use --force)"
            continue
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8", newline="\n") as f:
            f.write(page)
        entry["status"] = "written"
        entry["page"] = "skills/m-reference/" + rel
    with open(os.path.join(args.out, "collect.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    for name, e in results.items():
        print(f"  {name}: {e['status']}")
    written = sum(1 for e in results.values() if e["status"] == "written")
    print(f"{written} of {len(by_file)} page(s) written.")
    return 0


def usage_of(path):
    """Tokens reported by dsh --json: the usage on each step_end, summed."""
    total = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            try:
                event = json.loads(line)
            except ValueError:
                continue
            if event.get("type") == "status" and event.get("phase") == "step_end":
                for k, v in (event.get("usage") or {}).items():
                    if isinstance(v, (int, float)):
                        total[k] = total.get(k, 0) + v
    return total


def cmd_report(args):
    answers = os.path.join(args.out, "answers")
    usage = {}
    for name in sorted(os.listdir(answers)) if os.path.isdir(answers) else []:
        if name.endswith(".jsonl"):
            for k, v in usage_of(os.path.join(answers, name)).items():
                usage[k] = usage.get(k, 0) + v
    runs_path = os.path.join(args.out, "runs.json")
    runs = json.load(open(runs_path, encoding="utf-8-sig")) if os.path.exists(runs_path) else []
    collected_path = os.path.join(args.out, "collect.json")
    collected = json.load(open(collected_path, encoding="utf-8")) if os.path.exists(collected_path) else {}
    report = {
        "runs": len(runs),
        "failed_runs": sum(1 for r in runs if r.get("exit") != 0),
        "seconds": round(sum(r.get("seconds", 0) for r in runs), 1),
        "usage": usage,
        "written": sum(1 for e in collected.values() if e.get("status") == "written"),
        "refused_unsafe": sum(1 for e in collected.values() if e.get("status", "").startswith("refused")),
        "results_dropped": sum(e.get("results_dropped", 0) for e in collected.values()),
    }
    print(json.dumps(report, indent=2))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("command", choices=["prompts", "collect", "report"])
    parser.add_argument("--out", required=True, help="the run's folder (keep it under lab/drafting/out/)")
    parser.add_argument("--force", action="store_true", help="collect: overwrite existing pages")
    args = parser.parse_args(argv)
    args.out = os.path.abspath(args.out)
    return {"prompts": cmd_prompts, "collect": cmd_collect, "report": cmd_report}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
