#!/usr/bin/env python3
"""CI validation for the powerquery-m-for-agents repo.

Checks, for every skill folder (a dir under the plugin's `skills/` containing SKILL.md):
  1. Frontmatter: name == folder, name is kebab-case, description starts with "Use when".
  2. The skill is referenced in INDEX.md.
Then, repo-wide:
  3. Every Python script under scripts/ and lab/ compiles.
  3b. The shipped plugin folder stays under 512 files, none over 256 KiB.
  4. m-reference integrity: catalog rows <-> packed library cards <-> notes all line up.
     Tolerates the pre-export state where generated/ does not exist yet.

Adapted from dax-for-agents. Run: python scripts/validate_skills.py
"""
import os
import re
import sys
import glob
import json
import subprocess

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed (pip install pyyaml)")
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
errors = []


def frontmatter(path):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", txt, re.S)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return {"__error__": str(e)}


# ---- 1 & 2: per-skill frontmatter + INDEX coverage ----
PLUGIN = os.path.join(ROOT, "plugins", "powerquery-m-for-agents")
SKILLS = os.path.join(PLUGIN, "skills")
skill_dirs = sorted(
    d for d in (os.listdir(SKILLS) if os.path.isdir(SKILLS) else [])
    if os.path.isfile(os.path.join(SKILLS, d, "SKILL.md"))
)
if not skill_dirs:
    errors.append("no skill folders found under skills/ (none contain SKILL.md)")

index_path = os.path.join(ROOT, "INDEX.md")
index_txt = ""
if os.path.exists(index_path):
    with open(index_path, encoding="utf-8") as f:
        index_txt = f.read()
if not index_txt:
    errors.append("INDEX.md missing or empty")

for d in skill_dirs:
    fm = frontmatter(os.path.join(SKILLS, d, "SKILL.md"))
    if fm is None:
        errors.append(f"{d}: missing YAML frontmatter")
        continue
    if "__error__" in fm:
        errors.append(f"{d}: invalid YAML frontmatter ({fm['__error__']})")
        continue
    name = fm.get("name")
    desc = (fm.get("description") or "").strip()
    if name != d:
        errors.append(f"{d}: frontmatter name '{name}' != folder name")
    if not name or not KEBAB.match(str(name)):
        errors.append(f"{d}: name '{name}' is not kebab-case")
    if not desc.lower().startswith("use when"):
        errors.append(f"{d}: description must start with 'Use when' (got: {desc[:40]!r})")
    if d not in index_txt:
        errors.append(f"{d}: not referenced in INDEX.md")

# ---- 3: every Python script compiles ----
py_scripts = glob.glob(os.path.join(ROOT, "scripts", "*.py")) + \
    glob.glob(os.path.join(ROOT, "lab", "*.py"))
for py in sorted(py_scripts):
    r = subprocess.run([sys.executable, "-m", "py_compile", py],
                       capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        errors.append(f"py_compile failed: {os.path.relpath(py, ROOT)}: {r.stderr.strip()}")

# ---- 3b: the shipped folder stays small ----
# Only plugins/powerquery-m-for-agents/ ships. The plugin directory holds a plugin of more than
# 512 files, or with a file over 256 KiB, for a reviewer ("Ship fewer files"): the cards and
# the examples are packed one file per category so neither happens.
MAX_FILES = 512
MAX_BYTES = 256 * 1024


def shipped_files(root):
    tracked = subprocess.run(["git", "-C", root, "ls-files", "-z", "--", PLUGIN],
                             capture_output=True, check=True).stdout.decode("utf-8").split("\0")
    return [t for t in tracked if t]


try:
    shipped = shipped_files(ROOT)
    if len(shipped) >= MAX_FILES:
        errors.append(f"the plugin folder ships {len(shipped)} files; the plugin directory holds "
                      f"one of {MAX_FILES} or more for review (pack, or move maintainer files out)")
    for rel in shipped:
        path = os.path.join(ROOT, rel)
        if os.path.isfile(path) and os.path.getsize(path) > MAX_BYTES:
            errors.append(f"{rel} is {os.path.getsize(path):,} bytes, over the 256 KiB a "
                          f"plugin file may weigh (split it)")
except (OSError, subprocess.CalledProcessError) as e:
    shipped = []
    errors.append(f"could not list the shipped files with git: {e}")

# ---- 4: m-reference integrity ----
REF = os.path.join(SKILLS, "m-reference")
GEN = os.path.join(REF, "generated")
lib_dir = os.path.join(GEN, "library")
notes_dir = os.path.join(REF, "notes")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import m_blocks  # noqa: E402


def stems(d):
    if not os.path.isdir(d):
        return set()
    return {os.path.splitext(f)[0] for f in os.listdir(d) if f.endswith(".md")}


# {card file stem: {function names with a section there}}
cards = {}
for stem in sorted(stems(lib_dir)):
    with open(os.path.join(lib_dir, stem + ".md"), encoding="utf-8") as f:
        cards[stem] = {name for name, _ in m_blocks.sync_shared().sections(f.read())}
carded = set().union(*cards.values()) if cards else set()
notes = stems(notes_dir)

try:
    cat = m_blocks.load_catalog()
    if cat is None:
        if cards:
            errors.append("generated/library/ has cards but catalog/ is missing - run the sync")
    else:
        functions = cat.get("functions", [])
        files = {fn.get("file") for fn in functions}
        # A note is written about a function the engine exported.
        for orphan in sorted(notes - files):
            errors.append(f"m-reference/notes/{orphan}.md is about no function in the catalogue")
        for fn in functions:
            card = fn.get("card")
            if fn.get("name") not in cards.get(card, ()):
                errors.append(f"catalog puts '{fn.get('name')}' in library/{card}.md, which has "
                              "no section for it - run the sync")
        for extra in sorted(carded - {fn.get("name") for fn in functions}):
            errors.append(f"generated/library/ has a section for '{extra}', not in the catalog")
        flagged = {fn.get("file") for fn in functions if fn.get("notes")}
        for bad in sorted(flagged - notes):
            errors.append(f"catalog flags '{bad}' as having notes but notes/{bad}.md is missing")
        # Each name the agent can look up sits in exactly the index its kind says, so a
        # hand edit or a half-written sync cannot hide a function from the lookup.
        expected = {
            "catalog.md": {fn.get("name") for fn in functions
                           if fn.get("kind", "library") == "library"},
            "connectors.md": {fn.get("name") for fn in functions
                              if fn.get("kind") == "connector"},
            "constants.md": {c.get("name") for c in cat.get("constants", [])},
        }
        for index, names in expected.items():
            path = os.path.join(GEN, index)
            if not os.path.exists(path):
                if names:
                    errors.append(f"generated/{index} is missing but the catalogue has "
                                  f"{len(names)} entries for it - run the sync")
                continue
            with open(path, encoding="utf-8") as f:
                listed = set(re.findall(r"^\| `([^`]+)` \|", f.read(), re.M))
            for missing in sorted(names - listed):
                errors.append(f"generated/{index} does not list '{missing}' from the catalogue")
            for extra in sorted(listed - names):
                errors.append(f"generated/{index} lists '{extra}', which the catalogue puts elsewhere")
except (OSError, ValueError, KeyError, AttributeError, TypeError) as e:
    errors.append(f"catalog/ is not readable: {e}")

# ---- report ----
if errors:
    print("SKILL VALIDATION FAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
state = (f"{len(carded)} cards in {len(cards)} files, {len(notes)} notes" if cards
         else "not exported yet")
print(f"OK: {len(skill_dirs)} skill(s) validated, {len(py_scripts)} script(s) compiled, "
      f"{len(shipped)} file(s) shipped, m-reference: {state}.")
