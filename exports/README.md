# Exports

Raw output of `skills/m-reference/scripts/export_shared.pq`, one file per host and build:
`<host>-<version>.json`. Kept in the repo so every generation can be reproduced from the
exact input it came from.

The sync reads two more inputs from here:

| File | What it is |
|---|---|
| `vscode-powerquery-standard-enUs.json` | Microsoft's standard library file (MIT), the only source of the one-line descriptions. Commit in `THIRD_PARTY_NOTICES.md` |
| `learn-links.json` | The functions whose Microsoft Learn page answered 200, from `lab/shared-export/learn_links.py` |

The JSON files here are `export-ignore`: they stay in the repo and out of the plugin archive.
