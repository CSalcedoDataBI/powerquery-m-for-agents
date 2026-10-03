# Exports

Raw output of `skills/m-reference/scripts/export_shared.pq`, one file per host and build:
`<host>-<version>.json`, kept so every generation can be reproduced from the exact input it
came from.

**The JSON files are not in this public repository.** They are the maintainer's working
material and live in a private repository; here `exports/*.json` is in `.gitignore`, so
`sync_shared.py` and `learn_links.py` read and write them in this folder as before. This
README stays to say what they are.

The sync reads two more inputs from here:

| File | What it is |
|---|---|
| `vscode-powerquery-standard-enUs.json` | Microsoft's standard library file (MIT), the only source of the one-line descriptions. Commit in `THIRD_PARTY_NOTICES.md` |
| `learn-links.json` | The functions whose Microsoft Learn page answered 200, from `lab/shared-export/learn_links.py` |

## Microsoft's texts in the raw exports

A `<host>-<version>.json` file is the output of `export_shared.pq`, read from the engine's
`#shared` in Power BI Desktop (or another host): the exporter keeps the functions and the
metadata fields it needs, writes types as plain strings and splits the JSON into parts.
Besides the facts the sync uses (names, signatures, types, categories), each function
carries the documentation text Microsoft ships inside the engine: `description`,
`longDescription` and `examples`. That text is © Microsoft and is kept, privately, as the engine
returns it, with this attribution, only as the reproducible input of the catalogue.

`sync_shared.py` reads none of those three fields. The cards do not quote the long
descriptions or the examples, and link Microsoft Learn for them when that page exists. Their one-line descriptions
come from the MIT file above; for many functions that line is word for word the same as the
export's `description`, but the MIT file is where the cards take it from
([ADR](../docs/decisions/2026-10-01-textos-con-licencia.md)).
