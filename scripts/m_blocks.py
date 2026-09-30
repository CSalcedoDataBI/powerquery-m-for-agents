"""The executed-example format shared by lab/runner/run_examples.py and check_examples.py.

Every ```m block in a skill's hand-written pages is run in the engine, and the value the
engine returned sits in the ```text block right after it (blank lines allowed between):

    ```m
    Text.PadStart("7", 3, "0")
    ```

    ```text
    "007"
    ```

A page holding blocks carries one stamp line naming where they ran:

    <!-- lab: desktop 2.157.879.0 -->

The runner writes the results and the stamp; nobody types them.
"""
import os
import re
from dataclasses import dataclass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
STAMP_RE = re.compile(r"^<!-- lab: (?P<host>\S+) (?P<version>\S+) -->$", re.M)


@dataclass
class Block:
    code: str
    result: str | None
    code_start: int          # line index of the ```m fence
    code_end: int            # line index of its closing fence
    result_start: int | None
    result_end: int | None


def pages():
    """Hand-written Markdown under skills/, relative to ROOT. generated/ is the sync's."""
    found = []
    for dirpath, dirnames, filenames in os.walk(SKILLS):
        dirnames[:] = sorted(d for d in dirnames if d not in ("generated", "__pycache__"))
        for name in sorted(filenames):
            if name.endswith(".md"):
                found.append(os.path.relpath(os.path.join(dirpath, name), ROOT).replace("\\", "/"))
    return found


def _fence_end(lines, start):
    for j in range(start + 1, len(lines)):
        if lines[j].rstrip() == "```":
            return j
    raise ValueError(f"unclosed code fence at line {start + 1}")


def find_blocks(text):
    lines = text.split("\n")
    blocks, i = [], 0
    while i < len(lines):
        if lines[i].rstrip() == "```m":
            end = _fence_end(lines, i)
            code = "\n".join(lines[i + 1:end])
            k = end + 1
            while k < len(lines) and not lines[k].strip():
                k += 1
            if k < len(lines) and lines[k].rstrip() == "```text":
                r_end = _fence_end(lines, k)
                blocks.append(Block(code, "\n".join(lines[k + 1:r_end]), i, end, k, r_end))
                i = r_end + 1
            else:
                blocks.append(Block(code, None, i, end, None, None))
                i = end + 1
        else:
            i += 1
    return blocks


def stamp(text):
    m = STAMP_RE.search(text)
    return (m.group("host"), m.group("version")) if m else None


def apply_results(text, results, host, version):
    """`results` lists one engine result per block, in order. Returns the page with each
    block's ```text block written (replaced or inserted) and the stamp set."""
    blocks = find_blocks(text)
    if len(results) != len(blocks):
        raise ValueError(f"{len(blocks)} blocks but {len(results)} results")
    lines = text.split("\n")
    # Bottom-up, so earlier line indexes stay valid.
    for block, result in reversed(list(zip(blocks, results))):
        new = ["```text", *result.split("\n"), "```"]
        if block.result_start is None:
            lines[block.code_end + 1:block.code_end + 1] = ["", *new]
        else:
            lines[block.result_start:block.result_end + 1] = new
    out = "\n".join(lines)
    line = f"<!-- lab: {host} {version} -->"
    if STAMP_RE.search(out):
        out = STAMP_RE.sub(line, out, count=1)
    else:
        out = line + "\n\n" + out
    return out
