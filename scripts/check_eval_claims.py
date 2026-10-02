#!/usr/bin/env python3
"""Fail when the README's invention table and the saved runs disagree.

Every number in the README is counted from the tree (CLAUDE.md). The invention table is
counted from the answers committed under evals/hallucination/runs/: recounting them is a
lookup against the catalogue, with no model and no API call, so this runs in CI.

It also catches the counter changing. If the way an invention is counted is edited, every
number in the table moves, and this is what says so. Ported from dax-for-agents.

  python scripts/check_eval_claims.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(ROOT, "evals", "hallucination", "runs")
README = os.path.join(ROOT, "README.md")
sys.path.insert(0, os.path.join(ROOT, "evals", "hallucination"))

import run_ab  # noqa: E402

# `| Claude Haiku 4.5 | 35 | 10 | **6** |`: model, questions compared, arm A, arm B.
# Bold is emphasis, not data.
_ROW = re.compile(r"^\|\s*([A-Za-z][A-Za-z0-9.\- ]+?)\s*\|\s*\**(\d+)\**\s*\|"
                  r"\s*\**(\d+)\**\s*\|\s*\**(\d+)\**\s*\|\s*$", re.M)

# The README names models the way a person says them; the run files the way an API does.
MODEL_FILES = {
    "Claude Haiku 4.5": "2026-10-02-claude-haiku-4-5.json",
    "Claude Sonnet 5.5": "2026-10-02-claude-sonnet-5-5.json",
    "DeepSeek V4-Pro": "2026-10-02-deepseek-v4-pro.json",
    "DeepSeek V4-Flash": "2026-10-02-deepseek-v4-flash.json",
}


def table_rows(path=README):
    """(model, compared, arm A, arm B) for every row of the invention table."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return [(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))
            for m in _ROW.finditer(text) if m.group(1) in MODEL_FILES]


def counted(filename, names):
    """(compared, arm A, arm B) recounted from the saved answers, over the questions both
    arms answered - the same pairing run_ab's report uses."""
    with open(os.path.join(RUNS, filename), encoding="utf-8") as f:
        records = json.load(f)["records"]
    by_regime = run_ab.summarise(records, names)
    return (sum(s["n"] for s in by_regime.values()),
            sum(s["A"] for s in by_regime.values()),
            sum(s["B"] for s in by_regime.values()))


def main():
    names, _ = run_ab.catalog_names()
    rows = table_rows()
    if not rows:
        print("ERROR: the README has no invention table this gate recognises. If it was "
              "removed on purpose, remove this gate in the same commit.")
        return 1

    problems = []
    for model, said_n, said_a, said_b in rows:
        try:
            got = counted(MODEL_FILES[model], names)
        except (OSError, ValueError, KeyError) as exc:
            problems.append(f"{model}: its run file cannot be read ({exc})")
            continue
        if (said_n, said_a, said_b) != got:
            problems.append(f"{model}: the README says {said_n} questions, {said_a} -> "
                            f"{said_b}; the saved answers count {got[0]} questions, "
                            f"{got[1]} -> {got[2]}")

    for model in sorted(set(MODEL_FILES) - {r[0] for r in rows}):
        problems.append(f"{model} has a run file and no row in the README table: publish it "
                        f"or delete the run, but do not keep a measurement the prose omits")

    if problems:
        print("ERROR: the README's invention table does not match the runs it came from:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"OK: the README's invention table matches all {len(rows)} saved run(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
