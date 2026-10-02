#!/usr/bin/env python3
"""Measure the one thing this library exists for: does the reference stop invented names?

Same design as dax-for-agents (its evals/hallucination/run_ab.py), ported to M. Issue #7.

## The shape

Every question is asked twice, of the same model:

    arm A   the question alone
    arm B   the question, plus the catalogue rows of its category

Arm B is deliberately NOT the card that holds the answer. Handing over the answer would
measure obedience, not invention. The rows are the first hop SKILL.md documents (search the
catalogue, find the function), so arm B knows what exists and still has to choose.

## The metric is mechanical

No model judges another. In the CODE of an answer (fenced blocks and inline spans), every
dotted name (Table.AddColumn, BinaryFormat.Byte, Int64.Type) and every # literal (#date,
#table) is looked up. A dotted name that is not a function or constant of the export is an
invented one; a # literal that is not M syntax is too. Text literals, comments and quoted
step names are blanked first, with the same scanner the example check uses
(scripts/m_blocks.py), so "Sales.Amount" inside quotes or #"Added Custom" never counts.

Known limit: the catalogue is one host (Power BI Desktop). A name that exists only in Excel
(Excel.CurrentWorkbook does exist in Desktop; others may not) would count as invented. The
system prompt says Power BI Desktop for that reason, and #2 adds the second host.

    python evals/hallucination/run_ab.py --limit 3          # a few questions
    python evals/hallucination/run_ab.py                    # the whole bank
    python evals/hallucination/run_ab.py --regime deep      # one regime
    python evals/hallucination/run_ab.py --replay out.json  # re-count, no API calls
    python evals/hallucination/run_ab.py --out r.json --resume   # finish an interrupted run

The provider is read from the model's name, and each one has its own key variable:
ANTHROPIC_API_KEY for `claude-*`, DEEPSEEK_API_KEY for `deepseek-*`. A key is read from the
environment and nowhere else: never passed on the command line, never printed, never
written into the output file.
"""
import argparse
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed (pip install pyyaml)")
    sys.exit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import m_blocks  # noqa: E402

CATALOG_DIR = os.path.join(ROOT, "skills", "m-reference", "generated", "catalog")
QUESTIONS = os.path.join(HERE, "questions.yaml")

# The # literals of the M grammar. #shared and #sections are environment, not library
# members, but they are real M and a model that writes them has invented nothing.
HASH_LITERALS = frozenset({
    "binary", "date", "datetime", "datetimezone", "duration", "table", "time",
    "infinity", "nan", "shared", "sections",
})
_HASH_RE = re.compile(r"(?<![\w#])#([A-Za-z]\w*)\b")
_DEFINED_RE = re.compile(r"\s*=(?![=>])")


def catalog_names(directory=CATALOG_DIR):
    """(names, rows by category): every function and constant name of the export, and the
    `name: summary` rows of each catalogue file, keyed by the file's stem."""
    names, rows = set(), {}
    for entry in sorted(os.listdir(directory)):
        if not entry.endswith(".json") or entry == "index.json":
            continue
        with open(os.path.join(directory, entry), encoding="utf-8") as f:
            data = json.load(f)
        items = data.get("functions", []) + data.get("constants", [])
        names |= {i["name"] for i in items}
        rows[entry[:-5]] = [f"- {i['name']}: {i.get('summary') or ''}".rstrip(": ")
                            for i in items]
    return names, rows


_FENCE = re.compile(r"```[^\n]*\n(.*?)```", re.S)
_INLINE = re.compile(r"`([^`\n]+)`")


def code_spans(text):
    """The parts of an answer that are CODE: fenced blocks and inline spans.

    Prose is left out on purpose. "e.g. Power.Query" or a file name in a sentence is not a
    model naming a function; a model naming one it believes in writes it as code.
    """
    text = text or ""
    fenced = _FENCE.findall(text)
    rest = _FENCE.sub(" ", text)
    return fenced + _INLINE.findall(rest)


def used_names(text):
    """Every distinct library-shaped name in the answer's code, in order of appearance:
    dotted names, and # literals written as `#name`."""
    seen, out = set(), []
    for span in code_spans(text):
        # Quoted identifiers are dropped, unlike in check_examples: in an answer, #"..." is a
        # step or column name the model chose (#"Sales.Amount"), not a library call.
        bare, _quoted = m_blocks.scan(span)
        # A field access such as [Sales.Amount] is a column name, not a library name.
        bare = re.sub(r"\[[^\[\]=,]*\]", " ", bare)
        # A name being DEFINED is not a library name either: a record field
        # (meta [Documentation.Name = "..."], the documented way to describe a custom
        # function) or a let variable. A dotted name followed by `=` (not `=>`) is one.
        found = [m.group(1) for m in m_blocks.DOTTED_RE.finditer(bare)
                 if not _DEFINED_RE.match(bare, m.end())]
        found += ["#" + h for h in _HASH_RE.findall(bare)]
        for name in found:
            if name not in seen:
                seen.add(name)
                out.append(name)
    return out


# Documentation.Name, Documentation.Examples...: the metadata record fields that document a
# function, read by export_shared.pq from every function type. No #shared member has this
# prefix, so a model writing one (often in prose backticks) is naming a field, not inventing
# a library function. This eval measures library names only.
METADATA_PREFIXES = ("Documentation.",)


def invented(text, names):
    """The names used in code that are neither in the export nor M syntax."""
    bad = []
    for name in used_names(text):
        if name.startswith(METADATA_PREFIXES):
            continue
        if name.startswith("#"):
            if name[1:] not in HASH_LITERALS:
                bad.append(name)
        elif name not in names:
            bad.append(name)
    return bad


# Generous on purpose: a reasoning model spends budget thinking, and an empty answer
# scores zero inventions -- the best possible result, for not having answered.
MAX_TOKENS = 4000

SYSTEM = ("You are a Power Query developer working in Power BI Desktop, answering a "
          "colleague. Be brief: name the M functions involved and show a short snippet. "
          "Do not hedge with lists of alternatives you are unsure about.")


def _user(question, reference):
    if not reference:
        return question
    return (f"{question}\n\n---\nPower Query M functions available in this category, from "
            f"the language reference:\n\n{reference}")


def _anthropic_request(model, question, reference, system, max_tokens):
    return {"model": model, "max_tokens": max_tokens, "system": system,
            "messages": [{"role": "user", "content": _user(question, reference)}]}


def _anthropic_read(out):
    usage = dict(out.get("usage", {}))
    usage["stop_reason"] = out.get("stop_reason")
    text = "".join(b.get("text", "") for b in out.get("content", []))
    return text, usage


def _openai_request(model, question, reference, system, max_tokens):
    return {"model": model, "max_tokens": max_tokens,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": _user(question, reference)}]}


def _openai_read(out):
    choice = (out.get("choices") or [{}])[0]
    raw = out.get("usage", {}) or {}
    usage = {"input_tokens": raw.get("prompt_tokens", 0),
             "output_tokens": raw.get("completion_tokens", 0),
             "stop_reason": choice.get("finish_reason")}
    return (choice.get("message") or {}).get("content") or "", usage


PROVIDERS = {
    "anthropic": {
        "prefixes": ("claude-",),
        "url": "https://api.anthropic.com/v1/messages",
        "key_env": "ANTHROPIC_API_KEY",
        "headers": lambda key: {"x-api-key": key, "anthropic-version": "2023-06-01",
                                "content-type": "application/json"},
        "request": _anthropic_request,
        "read": _anthropic_read,
    },
    "deepseek": {
        "prefixes": ("deepseek-",),
        "url": "https://api.deepseek.com/chat/completions",
        "key_env": "DEEPSEEK_API_KEY",
        "headers": lambda key: {"Authorization": f"Bearer {key}",
                                "content-type": "application/json"},
        "request": _openai_request,
        "read": _openai_read,
    },
}


def provider_for(model):
    """The provider that serves this model, by name. Unknown stops the run."""
    for name, spec in PROVIDERS.items():
        if model.startswith(spec["prefixes"]):
            return name, spec
    raise SystemExit(
        f"ERROR: no provider is configured for '{model}'. Known prefixes: "
        + ", ".join(p for s in PROVIDERS.values() for p in s["prefixes"]))


def ask(model, key, question, reference=None, timeout=180):
    import urllib.request
    _, spec = provider_for(model)
    body = json.dumps(spec["request"](model, question, reference, SYSTEM, MAX_TOKENS)
                      ).encode()
    req = urllib.request.Request(spec["url"], data=body, headers=spec["headers"](key))
    with urllib.request.urlopen(req, timeout=timeout) as r:
        out = json.load(r)
    return spec["read"](out)


def describe(exc):
    """An API failure in the words the API used, so a 402 and a 401 do not look alike."""
    import urllib.error
    if isinstance(exc, urllib.error.HTTPError):
        try:
            body = json.loads(exc.read().decode("utf-8", "replace"))
            message = (body.get("error") or {}).get("message") or json.dumps(body)[:200]
        except Exception:                                     # noqa: BLE001
            message = exc.reason
        return f"HTTP {exc.code}: {message}"
    return f"{type(exc).__name__}: {exc}"


def answered(rec):
    """Both arms said something. Only these questions are compared.

    An empty arm scores zero inventions for saying nothing, which would flatter whichever
    arm went quiet. A model that refuses a question (stop_reason "refusal": Sonnet 5.5 does,
    on Expression.Evaluate) answered neither arm in any useful sense, so the pair is dropped
    and counted on its own line instead."""
    return all((rec[arm].get("text") or "").strip() for arm in ("A", "B"))


def summarise(records, names):
    """Per-regime counts for both arms, over the questions both arms answered. Never
    averaged across regimes: see questions.yaml."""
    by_regime = {}
    for rec in records:
        slot = by_regime.setdefault(rec["regime"], {"n": 0, "A": 0, "B": 0,
                                                    "A_q": 0, "B_q": 0, "dropped": 0})
        if not answered(rec):
            slot["dropped"] += 1
            continue
        slot["n"] += 1
        for arm in ("A", "B"):
            bad = invented(rec[arm]["text"], names)
            slot[arm] += len(bad)
            slot[arm + "_q"] += 1 if bad else 0
    return by_regime


def silent(records):
    """Answers with no text at all, per arm: they score zero inventions for saying nothing."""
    return {arm: sum(1 for r in records if not (r[arm]["text"] or "").strip())
            for arm in ("A", "B")}


def refusals(records):
    """The empty answers the provider marked as a refusal, as `id arm` strings."""
    return [f"{r['id']} {arm}" for r in records for arm in ("A", "B")
            if not (r[arm].get("text") or "").strip()
            and r[arm].get("stop_reason") == "refusal"]


def report(records, names):
    print()
    print(f"{'question':<28} {'regime':<6} {'invented A':>11} {'invented B':>11}")
    print("-" * 60)
    for rec in records:
        a = invented(rec["A"]["text"], names)
        b = invented(rec["B"]["text"], names)
        print(f"{rec['id']:<28} {rec['regime']:<6} {len(a):>11} {len(b):>11}")
        if a:
            print(f"{'':<28} A invented: {', '.join(a)}")
        if b:
            print(f"{'':<28} B invented: {', '.join(b)}")
    print()
    by_regime = summarise(records, names)
    print(f"{'regime':<10} {'questions':>9} {'A invented':>11} {'B invented':>11} "
          f"{'A q. with':>10} {'B q. with':>10} {'dropped':>8}")
    print("-" * 77)
    for regime in sorted(by_regime):
        s = by_regime[regime]
        print(f"{regime:<10} {s['n']:>9} {s['A']:>11} {s['B']:>11} "
              f"{s['A_q']:>10} {s['B_q']:>10} {s['dropped']:>8}")
    total_a = sum(s["A"] for s in by_regime.values())
    total_b = sum(s["B"] for s in by_regime.values())
    compared = sum(s["n"] for s in by_regime.values())
    dropped = sum(s["dropped"] for s in by_regime.values())
    print("-" * 77)
    print(f"{'TOTAL':<10} {compared:>9} {total_a:>11} {total_b:>11} {'':>10} {'':>10} "
          f"{dropped:>8}")

    refused = refusals(records)
    if refused:
        print(f"\nREFUSED by the model ({len(refused)} answer(s)): {', '.join(refused)}")
    other = [(f"{r['id']} {arm}", r[arm].get("stop_reason")) for r in records
             for arm in ("A", "B") if not (r[arm].get("text") or "").strip()
             and r[arm].get("stop_reason") != "refusal"]
    if other:
        # "length" is a reasoning model spending the whole budget thinking; no stop reason
        # at all is a failed call, which --resume asks again.
        print(f"\nEMPTY, not refused ({len(other)} answer(s)): "
              + ", ".join(f"{name} ({reason or 'no stop reason: re-ask with --resume'})"
                          for name, reason in other))
    if dropped:
        print(f"\n{dropped} question(s) dropped: a question is compared only when both arms "
              f"answered.")
    return total_a, total_b


def save(path, model, provider, records):
    """Write the run file after every question, so an interruption loses nothing paid for."""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"model": model, "provider": provider, "records": records}, f,
                  ensure_ascii=False, indent=2)


def already_answered(path):
    """Questions a previous run of this file finished, by id.

    An arm is finished when it has text, or when it is empty with a recorded stop reason (a
    refusal is an answer: asking again gets the same refusal). An empty arm with no stop
    reason is a failure or an older run file, and its question is asked again."""
    if not path or not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            saved = json.load(f)
    except (OSError, ValueError):
        return {}

    def finished(arm):
        return arm is not None and ((arm.get("text") or "").strip()
                                    or arm.get("stop_reason"))
    return {r["id"]: r for r in saved.get("records", [])
            if finished(r.get("A")) and finished(r.get("B"))}


def load_questions(path=QUESTIONS):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)["questions"]


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, help="ask only the first N questions")
    ap.add_argument("--regime", help="core | deep")
    ap.add_argument("--model", default=os.environ.get("EVAL_MODEL",
                                                      "claude-haiku-4-5-20251001"))
    ap.add_argument("--out", help="write every answer to this JSON file")
    ap.add_argument("--replay", help="re-count a saved run, making no API calls")
    ap.add_argument("--resume", action="store_true",
                    help="keep the answers already in --out and ask only what is missing")
    args = ap.parse_args(argv)

    names, rows = catalog_names()

    if args.replay:
        with open(args.replay, encoding="utf-8") as f:
            saved = json.load(f)
        print(f"replaying {len(saved['records'])} question(s) from {args.replay} "
              f"(model {saved.get('model', '?')}) - no API calls.")
        report(saved["records"], names)
        return 0

    questions = load_questions()
    if args.regime:
        questions = [q for q in questions if q["regime"] == args.regime]
    if args.limit:
        questions = questions[:args.limit]
    if not questions:
        print("no questions selected.")
        return 2

    provider, spec = provider_for(args.model)
    key = os.environ.get(spec["key_env"])
    if not key:
        print(f"ERROR: {spec['key_env']} is not set in the environment "
              f"({args.model} is served by {provider}).")
        return 2

    print(f"model {args.model} ({provider}) - {len(questions)} question(s) - 2 arms "
          f"each = {len(questions) * 2} calls")
    done = already_answered(args.out) if args.resume else {}
    if done:
        print(f"  resuming: {len(done)} question(s) already answered in {args.out}")
    records = [done[q["id"]] for q in questions if q["id"] in done]
    tokens_in, tokens_out = 0, 0
    consecutive = 0
    for q in questions:
        if q["id"] in done:
            continue
        reference = "\n".join(rows[q["category"]])
        rec = {"id": q["id"], "regime": q["regime"], "category": q["category"],
               "question": q["question"]}
        for arm, ref in (("A", None), ("B", reference)):
            try:
                text, usage = ask(args.model, key, q["question"], ref)
                consecutive = 0
            except Exception as exc:                          # noqa: BLE001
                consecutive += 1
                print(f"  {q['id']} arm {arm}: FAILED - {describe(exc)}")
                text, usage = "", {}
            rec[arm] = {"text": text, "stop_reason": usage.get("stop_reason")}
            tokens_in += usage.get("input_tokens", 0)
            tokens_out += usage.get("output_tokens", 0)
        if consecutive >= 4:
            # Four failures in a row is a condition (no balance, a rejected key), not a blip,
            # and a run of empty answers would report a perfect score.
            print(f"\n{consecutive} calls failed in a row. Stopping: a run of empty answers "
                  f"is not a measurement.")
            if args.out and records:
                save(args.out, args.model, provider, records)
                print(f"the {len(records)} question(s) already answered are kept in "
                      f"{args.out}; re-run with --resume once it is fixed.")
            return 2
        records.append(rec)
        if args.out:
            save(args.out, args.model, provider, records)
        a = len(invented(rec["A"]["text"], names))
        b = len(invented(rec["B"]["text"], names))
        print(f"  {q['id']:<28} A={a} B={b}", flush=True)

    report(records, names)
    print(f"\ntokens: {tokens_in} in, {tokens_out} out")
    if args.out:
        save(args.out, args.model, provider, records)
        print(f"answers written to {args.out} - re-count with --replay")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
