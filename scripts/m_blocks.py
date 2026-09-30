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


# What a block may call. The runner evaluates every block with Expression.Evaluate over
# #shared in the maintainer's own Power BI Desktop, so a block is code run on that machine:
# one that reads a file or calls a URL would do it there. Blocks are limited to library
# functions that compute on values, by the category the export gives each function.
PURE_CATEGORIES = {
    "Binary", "Binary Formats", "Combiner", "Comparer", "Date", "DateTime", "DateTimeZone",
    "Duration", "Error", "Function", "Lines", "List", "Logical", "Metadata", "Number",
    "Record", "Replacer", "Splitter", "Table", "Text", "Time", "Type", "Uri", "Values",
}
# Internal hooks (Embedded.Value, Variable.Value, Value.Firewall): off, except the one a page
# is about. Value.NativeQuery sends a query to a data source; Function.InvokeAfter stalls the
# runner for as long as the block asks; Table.FilterWithDataTable looks a variable up by the
# name it is given as text, the lookup Variable.Value does.
IMPURE_CATEGORIES = {"Values.Implementation"}
IMPURE_NAMES = {"Value.NativeQuery", "Function.InvokeAfter", "Table.FilterWithDataTable"}
# Parsers of text or binary values. Every way to fetch that value (File.Contents, Web.Contents)
# is refused, so what they parse can only be a literal of the block.
# Expression.Constant and Expression.Identifier only write M source as text, Value.Expression
# returns a value's syntax tree; evaluating any of it is
# Expression.Evaluate, which stays refused with the rest of its category.
PURE_NAMES = {"Table.WithErrorContext", "Csv.Document", "Json.Document", "Xml.Document",
              "Xml.Tables", "Expression.Constant", "Expression.Identifier", "Value.Expression"}
# Values that describe the machine the runner is on, which a result would publish: its time
# zone, its clock, its culture (the reason #shared exports TimeZone.Current as null).
MACHINE_NAMES = {"DateTime.LocalNow", "DateTime.FixedLocalNow", "DateTimeZone.LocalNow",
                 "DateTimeZone.FixedLocalNow", "DateTimeZone.UtcNow", "DateTimeZone.FixedUtcNow",
                 "DateTimeZone.ToLocal", "Culture.Current", "TimeZone.Current"}
ESCAPE_RE = re.compile(r"#\(([^()]*)\)")
SINGLE_ESCAPES = {"cr": chr(13), "lf": chr(10), "tab": chr(9), "#": "#"}
# An M identifier with dots: a letter or underscore, then letters, digits, underscores, in
# any script (My_Connector.Contents, Ñandú.X), and every dotted segment of it.
DOTTED_RE = re.compile(r"(?<![\w.])([^\W\d]\w*(?:\.\w+)+)(?![\w])")
ENVIRONMENT_RE = re.compile(r"#(shared|sections)\b")


def scan(code):
    """(code, quoted): the code with text literals and comments blanked out, and the names it
    writes as quoted identifiers. #"Web.Contents" is the same name as Web.Contents, so a
    check that blanks every "..." misses it."""
    out, quoted, i, n = [], [], 0, len(code)
    while i < n:
        if code.startswith("//", i):
            j = code.find("\n", i)
            i = n if j < 0 else j
            out.append(" ")
        elif code.startswith("/*", i):
            # Delimited comments nest in M: /* a /* b */ c */ is one comment.
            depth, i = 1, i + 2
            while i < n and depth:
                if code.startswith("/*", i):
                    depth, i = depth + 1, i + 2
                elif code.startswith("*/", i):
                    depth, i = depth - 1, i + 2
                else:
                    i += 1
            out.append(" ")
        elif code[i] == '"' or code.startswith('#"', i) or code.startswith('#!"', i):
            # "text", #"quoted identifier", #!"verbatim literal" (text as well).
            ident = code.startswith('#"', i)
            k, buf = i + (2 if ident else 3 if code[i] == "#" else 1), []
            while k < n:
                if code[k] == '"':
                    if code.startswith('""', k):
                        buf.append('"')
                        k += 2
                        continue
                    break
                buf.append(code[k])
                k += 1
            if ident:
                quoted.append("".join(buf))
            out.append(" " if ident else '""')
            i = k + 1
        else:
            out.append(code[i])
            i += 1
    return "".join(out), [unescape(q) for q in quoted]


def unescape(text):
    """A quoted identifier or text literal as M reads it: #(002E) is ".", #(cr,lf) two
    characters. #"File#(002E)Contents" is File.Contents. An escape M would reject is kept."""
    def one(m):
        out = []
        for part in m.group(1).split(","):
            if part in SINGLE_ESCAPES:
                out.append(SINGLE_ESCAPES[part])
            elif re.fullmatch(r"[0-9A-Fa-f]{4}|[0-9A-Fa-f]{8}", part) and int(part, 16) <= 0x10FFFF:
                out.append(chr(int(part, 16)))
            else:
                return m.group(0)
        return "".join(out)
    return ESCAPE_RE.sub(one, text)


def unsafe_calls(code, catalog, unknown=False):
    """What in one ```m block could reach outside the engine: the environment itself
    (#shared, #sections) and any exported function outside PURE_CATEGORIES - data sources,
    connectors, Expression.Evaluate - and the names in MACHINE_NAMES.

    A dotted name the export does not have is left to the invented-name check, unless
    `unknown` is set. The runner sets it: it evaluates against the live #shared of whatever
    Desktop is open, which can hold a connector the committed export does not, so a name
    this check cannot classify is refused before anything runs."""
    functions = {r["name"]: r for r in catalog.get("functions", [])}
    known = set(functions) | {c["name"] for c in catalog.get("constants", [])}
    bare, quoted = scan(code)
    found = [f"#{m}" for m in ENVIRONMENT_RE.findall(bare)]
    # Section access (Section1!Query) reads the query document; M has no other use for "!".
    if "!" in bare:
        found.append("section access (!)")
    for name in sorted(set(DOTTED_RE.findall(bare)) | set(quoted)):
        if name in MACHINE_NAMES:
            found.append(name)
            continue
        row = functions.get(name)
        if row is None:
            if unknown and name not in known and DOTTED_RE.fullmatch(name):
                found.append(name)
            continue
        category = row.get("category") or ""
        if name in PURE_NAMES:
            continue
        if (row.get("kind") != "library" or name in IMPURE_NAMES
                or category in IMPURE_CATEGORIES or category.split(".")[0] not in PURE_CATEGORIES):
            found.append(name)
    return found


def allowed_names(catalog):
    """Every exported name a block may use: the library functions and constants that
    unsafe_calls lets through. The runner evaluates each block against only these members
    of #shared, so a name the scan cannot see - a bare global such as another query - does
    not resolve either."""
    names = [r["name"] for r in catalog.get("functions", []) if r.get("kind") == "library"]
    names += [c["name"] for c in catalog.get("constants", [])]
    return sorted({n for n in names if not unsafe_calls(n, catalog)})
