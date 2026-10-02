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

## Microsoft's texts in the raw exports

A `<host>-<version>.json` file is the engine's `#shared` exactly as Power BI Desktop (or
another host) returns it. Besides the facts the sync uses (names, signatures, types,
categories), each function carries the documentation Microsoft ships inside the engine:
`description`, `longDescription` and `examples`. Those texts are © Microsoft and are kept
here unedited, with this attribution, only as the reproducible input of the catalogue.

`sync_shared.py` does not read them, and no card quotes them: the one-line descriptions come
from the MIT file above, and the cards link Microsoft Learn for the rest
([ADR](../docs/decisions/2026-10-01-textos-con-licencia.md)).
