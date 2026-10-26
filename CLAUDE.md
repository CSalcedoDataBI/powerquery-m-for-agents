# Agent instructions

This repository is **public**. Write every issue and commit for a public reader: no client
names, no real engagements, no credentials, no contents of private repositories.

**Only `plugins/powerquery-m-for-agents/` ships** to the plugin directory. Keep it under 512
files with nothing a maintainer alone needs (`scripts/validate_skills.py` checks the count).

## Rules specific to this repo

- **`plugins/powerquery-m-for-agents/skills/m-reference/generated/` and `catalog/` are written
  only by `scripts/sync_shared.py`.** Never edit a card by hand; write a note in `notes/`
  instead.
- **Never add a function name to anything an agent reads unless it came from a `#shared`
  export.** This library exists to stop invention; it cannot contain any.
- **Every number in the README is counted from the tree**, not typed. Until there is a check
  for a number, do not write that number.
- Repository language is English; specs and ADRs under `docs/` are in Spanish, as in
  dax-for-agents.

Conventions live in [INDEX.md](INDEX.md#conventions).
