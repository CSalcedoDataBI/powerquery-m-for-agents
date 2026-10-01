#!/usr/bin/env python3
"""Translate the function descriptions the review PBIPs show into Spanish, with an outside model.

  python lab/drafting/translate.py prompts --out lab/drafting/out/dsh-es   # 50 descriptions a prompt
  (run_dsh.ps1 answers each prompt in a container)
  python lab/drafting/translate.py collect --out lab/drafting/out/dsh-es   # -> lab/review/descriptions-es.json

The English is the engine's own documentation, from each library card (build_review.description).
A translation is taken only if it keeps what the English quotes as code: the same `names`, in the
same number, and the same numbers. It is stored with the English it was made from, so when a card
changes, build_review shows nothing for it until it is translated again.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "lab", "review"))
sys.path.insert(0, HERE)

import build_review  # noqa: E402
from pilot import final_text  # noqa: E402

TARGET = os.path.join(ROOT, "lab", "review", "descriptions-es.json")
CHUNK = 10

INSTRUCTIONS = """\
Translate each description of a Power Query M library function from English to Spanish.

Rules:
- Neutral, technical Spanish, as in Microsoft's Spanish documentation.
- Keep every `code span` exactly as written, backticks included: names of functions,
  parameters, types and values are never translated.
- Keep every number, and keep the "- name:" list items as they are, translating only their text.
- Answer with one JSON object only, mapping each key to its Spanish text: the same keys, no
  preamble, no explanation, no code fence, no tool calls.

=== Descriptions (JSON) ===
{items}
"""

CODE_RE = re.compile(r"`[^`]*`")
NUMBER_RE = re.compile(r"\d+(?:\.\d+)?")


def library():
    """{file: English description with its code spans} for every library function with a card."""
    with open(build_review.CATALOG, encoding="utf-8") as f:
        catalog = json.load(f)
    out = {}
    for r in sorted(catalog["functions"], key=lambda r: r["name"]):
        if r.get("kind") == "library":
            try:
                out[r["file"]] = build_review.description(r["file"], code=True)
            except SystemExit:
                continue
    return out


def load_target():
    if not os.path.exists(TARGET):
        return {}
    with open(TARGET, encoding="utf-8") as f:
        return json.load(f)


def cmd_prompts(args):
    done = load_target()
    todo = {k: v for k, v in library().items() if done.get(k, {}).get("en") != v}
    folder = os.path.join(args.out, "prompts")
    os.makedirs(folder, exist_ok=True)
    keys = sorted(todo)
    for n, i in enumerate(range(0, len(keys), CHUNK)):
        items = {k: todo[k] for k in keys[i:i + CHUNK]}
        with open(os.path.join(folder, f"es-{n + 1:02d}.txt"), "w", encoding="utf-8", newline="\n") as f:
            f.write(INSTRUCTIONS.format(items=json.dumps(items, ensure_ascii=False, indent=1)))
    print(f"{len(keys)} description(s) to translate in {-(-len(keys) // CHUNK)} prompt(s) under {folder}")
    return 0


def why_not(en, es):
    """Why a translation is refused, or None."""
    if not isinstance(es, str) or not es.strip():
        return "empty"
    if sorted(CODE_RE.findall(en)) != sorted(CODE_RE.findall(es)):
        return "code spans differ"
    if sorted(NUMBER_RE.findall(CODE_RE.sub("", en))) != sorted(NUMBER_RE.findall(CODE_RE.sub("", es))):
        return "numbers differ"
    if re.search(r"<[A-Za-z!/]|://|www\.", es) and not re.search(r"<[A-Za-z!/]|://|www\.", en):
        return "HTML or a link"
    return None


def cmd_collect(args):
    english = library()
    target = load_target()
    answers = os.path.join(args.out, "answers")
    taken, refused = 0, []
    for name in sorted(os.listdir(answers)):
        if not name.endswith(".jsonl"):
            continue
        text = final_text(os.path.join(answers, name)) or ""
        text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())
        try:
            answer = json.loads(text)
        except ValueError:
            refused.append(f"{name}: not JSON")
            continue
        for file, es in answer.items():
            en = english.get(file)
            if en is None:
                refused.append(f"{file}: not a library function")
                continue
            why = why_not(en, es)
            if why:
                refused.append(f"{file}: {why}")
                continue
            target[file] = {"en": en, "es": es.strip()}
            taken += 1
    with open(TARGET, "w", encoding="utf-8", newline="\n") as f:
        json.dump(dict(sorted(target.items())), f, ensure_ascii=False, indent=1)
        f.write("\n")
    missing = sorted(k for k, v in english.items() if target.get(k, {}).get("en") != v)
    for r in refused:
        print("  refused", r)
    print(f"{taken} taken, {len(refused)} refused, {len(missing)} still without a current translation.")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("command", choices=["prompts", "collect"])
    parser.add_argument("--out", required=True, help="the run's folder (keep it under lab/drafting/out/)")
    args = parser.parse_args(argv)
    args.out = os.path.abspath(args.out)
    return {"prompts": cmd_prompts, "collect": cmd_collect}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
