# Maintaining m-reference

For contributors. An agent answering a question about M never needs this page.

## Regenerating

**Power BI Desktop, automated** (from the repo root, with Desktop closed or open on
something else — the script only touches the engine it starts):

```bash
python lab/shared-export/build_pbip.py --host desktop --host-version <Desktop build>
powershell.exe -ExecutionPolicy Bypass -File lab/shared-export/export_desktop.ps1
```

**Any other host, by hand:**

1. Paste `scripts/export_shared.pq` into a blank query in the host; set `Host` and
   `HostVersion`.
2. Save the resulting JSON (concatenate the `json` chunks in `part` order, or save the chunk
   table as JSON — the sync accepts both) to `exports/<host>-<version>.json`.

Then report, and write:

```bash
python scripts/sync_shared.py exports/desktop.json exports/excel.json
python scripts/sync_shared.py exports/desktop.json exports/excel.json --write
```

The descriptions are not the engine's: only Microsoft's MIT-licensed standard library file
is quoted (#1). The sync reads it from `exports/vscode-powerquery-standard-enUs.json`
(`--descriptions`) and the checked Microsoft Learn pages from `exports/learn-links.json`
(`--learn-links`). To refresh them:

```bash
gh api "repos/microsoft/vscode-powerquery/contents/server/src/library/standard/standard-enUs.json?ref=<commit>" \
  -H "Accept: application/vnd.github.raw" > exports/vscode-powerquery-standard-enUs.json
python lab/shared-export/learn_links.py exports/learn-links.json
```

Then record the commit in `plugins/powerquery-m-for-agents/THIRD_PARTY_NOTICES.md`.

The first export named wins each card; the rest only contribute `hosts`. Gates: an export
with fewer than 100 functions, two names mapping to one file, an orphan note, or the count
moving more than 5% (override with `--accept-count-change`). The new tree is built in a
scratch directory and swapped in one move.

What it writes: the plugin's `generated/` (the three indexes, and `library/<part>.md` with
every card of one catalogue part as a `## <Name>` section, continued in `<part>-2.md` past
256 KiB) and `catalog/` at the repository root (the JSON catalogue the scripts read; it does
not ship). The plugin directory holds a plugin of 512 files or more for review, which is why
the cards are packed: `scripts/validate_skills.py` fails the build at that count.

## Running the examples

Every ```` ```m ```` block under the plugin's `skills/` is run by `lab/runner/run_examples.py` in Power BI
Desktop, each block in its own refresh, and its result written below it. Keep one Desktop
open for the session instead of one per run:

```bash
python lab/runner/run_examples.py --open
python lab/runner/run_examples.py --port <port> --write
python lab/runner/run_examples.py --port <port> --check
```

The port is the one Desktop's engine listens on (the `powerbi-modeling` MCP lists it as a
local instance). CI cannot run Desktop; `scripts/check_examples.py` checks there that every
block has a result, that examples sit under their card's category, and that every dotted
library name in these pages is in the export or was printed by the engine.

Examples are packed like the cards: `examples/<category>.md`, one `## <Name>` section per
function, in name order, under one `<!-- lab: ... -->` stamp at the top of the file (the
runner rewrites it when it writes results). To add a function, add its section to its
category's file (`lab/drafting/pilot.py collect` does it for drafted pages).
