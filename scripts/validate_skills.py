#!/usr/bin/env python3
"""CI validation for the powerquery-m-for-agents repo.

Checks, for every skill folder (a dir under `skills/` containing SKILL.md):
  1. Frontmatter: name == folder, name is kebab-case, description starts with "Use when".
  2. The skill is referenced in INDEX.md.
Then, repo-wide:
  3. Every Python script under skills/*/scripts/, scripts/ and lab/ compiles.
  4. m-reference integrity: catalog rows <-> library cards <-> notes all line up.
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
SKILLS = os.path.join(ROOT, "skills")
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
py_scripts = glob.glob(os.path.join(ROOT, "skills", "*", "scripts", "*.py")) + \
    glob.glob(os.path.join(ROOT, "scripts", "*.py")) + \
    glob.glob(os.path.join(ROOT, "lab", "*.py"))
for py in sorted(py_scripts):
    r = subprocess.run([sys.executable, "-m", "py_compile", py],
                       capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        errors.append(f"py_compile failed: {os.path.relpath(py, ROOT)}: {r.stderr.strip()}")

# ---- 4: m-reference integrity ----
REF = os.path.join(SKILLS, "m-reference")
GEN = os.path.join(REF, "generated")
cat_json = os.path.join(GEN, "catalog.json")
lib_dir = os.path.join(GEN, "library")
notes_dir = os.path.join(REF, "notes")


def stems(d):
    if not os.path.isdir(d):
        return set()
    return {os.path.splitext(f)[0] for f in os.listdir(d) if f.endswith(".md")}


cards = stems(lib_dir)
notes = stems(notes_dir)

# A note is written about a function the engine exported. Before the first export there is
# nothing to write a note about, so a note then is about a function nobody verified exists.
for orphan in sorted(notes - cards):
    errors.append(f"m-reference/notes/{orphan}.md has no generated/library/{orphan}.md")

if os.path.exists(cat_json):
    try:
        with open(cat_json, encoding="utf-8") as f:
            cat = json.load(f)
        rows = {fn.get("file") for fn in cat.get("functions", [])}
        for missing in sorted(rows - cards):
            errors.append(f"catalog lists '{missing}' but generated/library/{missing}.md is missing")
        for extra in sorted(cards - rows):
            errors.append(f"generated/library/{extra}.md exists but is not in the catalog")
        flagged = {fn.get("file") for fn in cat.get("functions", []) if fn.get("notes")}
        for bad in sorted(flagged - notes):
            errors.append(f"catalog flags '{bad}' as having notes but notes/{bad}.md is missing")
        # Each name the agent can look up sits in exactly the index its kind says, so a
        # hand edit or a half-written sync cannot hide a function from the lookup.
        expected = {
            "catalog.md": {fn.get("name") for fn in cat.get("functions", [])
                           if fn.get("kind", "library") == "library"},
            "connectors.md": {fn.get("name") for fn in cat.get("functions", [])
                              if fn.get("kind") == "connector"},
            "constants.md": {c.get("name") for c in cat.get("constants", [])},
        }
        for index, names in expected.items():
            path = os.path.join(GEN, index)
            if not os.path.exists(path):
                if names:
                    errors.append(f"generated/{index} is missing but catalog.json has "
                                  f"{len(names)} entries for it - run the sync")
                continue
            with open(path, encoding="utf-8") as f:
                listed = set(re.findall(r"^\| `([^`]+)` \|", f.read(), re.M))
            for missing in sorted(names - listed):
                errors.append(f"generated/{index} does not list '{missing}' from catalog.json")
            for extra in sorted(listed - names):
                errors.append(f"generated/{index} lists '{extra}', which catalog.json puts elsewhere")
    except (json.JSONDecodeError, AttributeError, TypeError) as e:
        errors.append(f"m-reference/generated/catalog.json is not readable: {e}")
elif cards:
    errors.append("generated/library/ has cards but generated/catalog.json is missing - run the sync")

# ---- report ----
if errors:
    print("SKILL VALIDATION FAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
state = f"{len(cards)} cards, {len(notes)} notes" if cards else "not exported yet"
print(f"OK: {len(skill_dirs)} skill(s) validated, {len(py_scripts)} script(s) compiled, "
      f"m-reference: {state}.")
