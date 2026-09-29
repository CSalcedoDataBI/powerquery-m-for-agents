# Agent instructions

This repository is **private for now and meant to go public** (see the
[design spec](docs/superpowers/specs/2026-09-28-powerquery-m-for-agents-design.md), §3).
Write every issue and commit as if it were already public: no client names, no real
engagements, no credentials, no contents of private repositories.

## Rules specific to this repo

- **`skills/m-reference/generated/` is written only by `sync_shared.py`.** Never edit a card
  by hand; write a note in `notes/` instead.
- **Never add a function name to anything an agent reads unless it came from a `#shared`
  export.** This library exists to stop invention; it cannot contain any.
- **Every number in the README is counted from the tree**, not typed. Until there is a check
  for a number, do not write that number.
- Repository language is English; specs and ADRs under `docs/` are in Spanish, as in
  dax-for-agents.

Conventions live in [INDEX.md](INDEX.md#conventions).
