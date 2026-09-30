#!/usr/bin/env python3
"""Run every ```m block of the skills in Power BI Desktop and write what the engine returned.

  python lab/runner/run_examples.py            # run, report which results changed
  python lab/runner/run_examples.py --write    # run, write the ```text blocks and stamps
  python lab/runner/run_examples.py --check    # run, exit 1 if any written result differs

All blocks go into one query (runner.pq) written to lab/runner/build/runner-query.pq. The
throwaway PBIP next to it has one partition that reads that file and evaluates it with
Expression.Evaluate over #shared. Without --port, each run opens Desktop, refreshes and
closes it. To keep one Desktop open for a whole session:

  python lab/runner/run_examples.py --open                       # once
  python lab/runner/run_examples.py --port N --write             # refreshes and reads
  python lab/runner/run_examples.py --prepare                    # or: write the query,
  #   refresh table ExamplesRunner yourself (e.g. the powerbi-modeling MCP), then
  python lab/runner/run_examples.py --port N --no-refresh --write

Windows only; the format is checked on CI by check_examples.py.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "lab", "shared-export"))

import m_blocks  # noqa: E402
from build_pbip import json_text, project_files, tmdl_source  # noqa: E402,F401

NAME = "ExamplesRunner"
BUILD = os.path.join(HERE, "build")
EXPORT = os.path.join(ROOT, "lab", "shared-export", "export_desktop.ps1")
DESKTOP = os.path.join(os.environ.get("ProgramFiles", r"C:\Program Files"),
                       "Microsoft Power BI Desktop", "bin", "PBIDesktop.exe")
RUNNER_IDS = {
    "generator": "lab/runner/run_examples.py from runner.pq",
    "model": "5a4ed000-0000-4000-8000-000000000201",
    "report": "5a4ed000-0000-4000-8000-000000000202",
    "table": "5a4ed000-0000-4000-8000-000000000301",
    "columns": ["5a4ed000-0000-4000-8000-000000000302", "5a4ed000-0000-4000-8000-000000000303",
                "5a4ed000-0000-4000-8000-000000000304"],
}


def m_text(value):
    """A Python string as an M text literal on one line."""
    v = value.replace("#(", "#(#)(").replace('"', '""')
    v = v.replace("\r", "#(cr)").replace("\n", "#(lf)").replace("\t", "#(tab)")
    return f'"{v}"'


def collect():
    """[(page, block index, code)] for every ```m block, plus the page texts."""
    cases, texts = [], {}
    for page in m_blocks.pages():
        with open(os.path.join(ROOT, page), encoding="utf-8") as f:
            text = f.read()
        blocks = m_blocks.find_blocks(text)
        if blocks:
            texts[page] = text
            cases += [(page, i, b.code) for i, b in enumerate(blocks)]
    return cases, texts


QUERY_FILE = os.path.join(BUILD, "runner-query.pq")
CASES_DIR = os.path.join(BUILD, "cases")


def query_text(cases):
    with open(os.path.join(HERE, "runner.pq"), encoding="utf-8") as f:
        query = f.read()
    listed = ", ".join("{" + m_text(f"{p}:{i}") + ", " + m_text(code) + "}" for p, i, code in cases)
    marker = "    Cases = {},"
    if query.count(marker) != 1:
        raise SystemExit("runner.pq no longer has exactly one 'Cases = {},' line")
    return query.replace(marker, f"    Cases = {{{listed}}},")


def write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def build(cases):
    write_text(QUERY_FILE, query_text(cases))
    query_file = QUERY_FILE
    # The partition only reads that file and evaluates it, so a Desktop left open on this
    # model picks up a new set of blocks on its next refresh: no reopening, no model edit.
    partition = (
        "let\n"
        f"    Query = Text.FromBinary(File.Contents({m_text(query_file)}), TextEncoding.Utf8)\n"
        "in\n"
        "    Expression.Evaluate(Query, #shared)")
    files = project_files(NAME, tmdl_source(partition),
                          [("seq", "int64"), ("id", "string"), ("result", "string")], RUNNER_IDS)
    for rel, text in files.items():
        path = os.path.join(BUILD, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\r\n") as f:
            f.write(text)
    return os.path.join(BUILD, f"{NAME}.pbip")


def run_isolated(cases, port):
    """Each case in its own refresh of the open model (see run_isolated.ps1 for why)."""
    shutil.rmtree(CASES_DIR, ignore_errors=True)
    for n, case in enumerate(cases):
        write_text(os.path.join(CASES_DIR, f"{n:05d}.pq"), query_text([case]))
    results = os.path.join(BUILD, "results.json")
    if os.path.exists(results):
        os.remove(results)
    subprocess.run(
        ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
         os.path.join(HERE, "run_isolated.ps1"), "-Port", str(port), "-CasesDir", CASES_DIR,
         "-QueryFile", QUERY_FILE, "-OutFile", results],
        check=True)
    with open(results, encoding="utf-8-sig") as f:
        rows = json.load(f)
    return {r["id"]: r["result"] for r in ([rows] if isinstance(rows, dict) else rows)}


def desktop_version():
    out = subprocess.run(
        ["powershell.exe", "-NoProfile", "-Command",
         f"(Get-Item '{DESKTOP}').VersionInfo.FileVersion"],
        capture_output=True, text=True, check=True)
    return out.stdout.strip()


def run(pbip, port=0, refresh=True):
    results = os.path.join(BUILD, "results.json")
    if os.path.exists(results):
        os.remove(results)
    cmd = ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", EXPORT,
           "-Pbip", pbip, "-Table", NAME, "-OrderBy", "seq", "-OutFile", results]
    cmd += ["-Port", str(port)] if port else ["-Close"]
    if not refresh:
        cmd.append("-NoRefresh")
    subprocess.run(cmd, check=True)
    with open(results, encoding="utf-8-sig") as f:
        rows = json.load(f)
    if isinstance(rows, dict):
        rows = [rows]
    return {r["id"]: r["result"] for r in rows}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--open", action="store_true",
                      help="build and open Desktop on the runner model, and leave it open")
    mode.add_argument("--prepare", action="store_true",
                      help="only write the query; refresh the open model yourself, then "
                           "--port N --no-refresh --write")
    parser.add_argument("--port", type=int, default=0,
                        help="read from a Desktop already open on the runner model")
    parser.add_argument("--no-refresh", action="store_true",
                        help="with --port: read without refreshing (refreshed elsewhere)")
    parser.add_argument("--batch", action="store_true",
                        help="with --port: evaluate every case in one refresh (fast, but cases "
                             "can leak into each other; see run_isolated.ps1)")
    parser.add_argument("--only", default="",
                        help="run only the pages whose path contains this text")
    args = parser.parse_args(argv)

    cases, texts = collect()
    if args.only:
        wanted = [w for w in args.only.split(",") if w]
        cases = [c for c in cases if any(w in c[0] for w in wanted)]
        texts = {p: t for p, t in texts.items() if any(w in p for w in wanted)}
    if not cases:
        print("No ```m blocks under skills/.")
        return 0
    print(f"{len(cases)} block(s) in {len(texts)} page(s).")
    pbip = build(cases)
    if args.prepare:
        print(f"Wrote {os.path.join(BUILD, 'runner-query.pq')}.")
        return 0
    if args.open:
        proc = subprocess.Popen([DESKTOP, pbip])
        print(f"Opened Desktop on {pbip} (PID {proc.pid}). Find its port, then run with --port.")
        return 0
    if args.port and not args.no_refresh and not args.batch:
        got = run_isolated(cases, args.port)
    else:
        print("WARNING: one evaluation for every case; cases can leak into each other. "
              "For results to publish, use --port N (isolated) on a Desktop left --open.")
        got = run(pbip, args.port, refresh=not args.no_refresh)
    version = desktop_version()

    changed, errors = [], []
    for page, text in texts.items():
        blocks = m_blocks.find_blocks(text)
        results = []
        for i, block in enumerate(blocks):
            key = f"{page}:{i}"
            if key not in got:
                raise SystemExit(f"the engine returned no row for {key}")
            results.append(got[key])
            if got[key] != block.result:
                changed.append(key)
            # A block that does not parse is a typo, never an example. The engine reports it as
            # Expression.Error with a source location and a "Token ... expected" message; an
            # unresolved name carries a location too, and that one can be the point of a page.
            if (got[key].startswith("error: ") and "Language.TextSourceLocation" in got[key]
                    and "Token " in got[key]):
                errors.append(f"{key}: {got[key]}")
        if args.write:
            new = m_blocks.apply_results(text, results, "desktop", version)
            if new != text:
                with open(os.path.join(ROOT, page), "w", encoding="utf-8", newline="\n") as f:
                    f.write(new)

    for e in errors:
        print(f"  SYNTAX {e}")
    print(f"{len(changed)} result(s) differ from the page"
          + (" - written." if args.write else "."))
    for key in changed[:50]:
        print(f"  {key}")
    if args.check and changed:
        return 1
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
