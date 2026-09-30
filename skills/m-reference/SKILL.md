---
name: m-reference
description: Use when you need to know whether a Power Query M library function exists, its exact signature and parameter types, what it returns, which hosts have it (Power BI Desktop, Excel, Dataflows Gen2), or which of several similar functions to reach for — and for the M language itself when no single function is in question, such as let/in, each and the underscore, records, lists and tables, types and metadata, try/otherwise/catch, lazy evaluation and streaming. The canonical reference for Power Query M. Triggers on "what does X do in M", "Power Query function signature", "is there an M function to", "Table.X vs Table.Y", "does X exist in Excel Power Query", "M syntax", "each _", "try otherwise", "Power Query types".
---

# M Reference

Every Power Query M library function, agent-native. The catalogue is **exported from the
engine itself** (`#shared`), not scraped from documentation: a function in the catalogue
exists in the host it names. See
[the design spec](../../docs/superpowers/specs/2026-09-28-powerquery-m-for-agents-design.md).

> **Status.** `generated/` is built from one export: Power BI Desktop (the host and build are
> in the header of `catalog.md`). No other host yet, so no card carries ⌂. No field notes or
> executed examples yet.

## How to use this

**One hop. Do not read the whole library.**

1. Read **`generated/catalog.md`**. Every library function, one row each: name, category,
   return type, flags, one-line summary. Looking for a connector (`Snowflake.Databases`,
   `Stripe.Contents`)? Read **`generated/connectors.md`** instead. A constant or type value
   (`JoinKind.Inner`, `Int64.Type`)? **`generated/constants.md`**, which already holds the
   whole answer: there are no constant cards.
2. Find the function. Open its card: **`generated/library/<file>.md`** (file naming below).
   Connector cards live there too.
3. Flag **★** → also read **`notes/<file>.md`**: field knowledge not in the engine metadata.
4. Flag **▶** → the card links to **`examples/<category>/<file>.md`**: queries executed in
   this repository's lab, each with the value the engine returned.
5. Flag **⌂** → the function is missing from at least one exported host. The card says
   which ones have it. Check before suggesting it for Excel or a dataflow.

**A name that is in none of `catalog.md`, `connectors.md` and `constants.md` does not exist
in any exported host.** Say so rather than offering it. That covers functions, connector
entry points and constants such as `GroupKind.Local` or `Occurrence.All`. One kind of name is
**not** covered, so its absence proves nothing:

- **Literal keywords** such as `#date`, `#table`, `#duration`. They are part of the language
  syntax, not library members.

A connector is a function the engine gives no category, under a prefix no library function
uses. Many carry no description. Data-access functions the engine documents (`Csv.Document`,
`Web.Contents`, `Sql.Database`, …) are library, in `catalog.md`.

The card section `## Examples (engine metadata — not verified here)` is copied from the
function's own `Documentation.Examples`. Useful for shape; not evidence.

## Layout

| Path | What it is |
|---|---|
| `generated/catalog.md` | The index the agent reads: library functions. **Generated** |
| `generated/connectors.md` | Connector entry points, same columns. **Generated** |
| `generated/constants.md` | Constants and type values, with their value. **Generated** |
| `generated/catalog.json` | All three indexes for scripts. **Generated**, never loaded into context |
| `generated/library/<file>.md` | One card per function or connector. **Generated — never edit by hand** |
| `notes/<file>.md` | Field notes. **Hand-written**; the sync never touches them |
| `examples/<category>/<file>.md` | Executed examples. **Hand-written** |
| `scripts/export_shared.pq` | The M query that dumps `#shared` (functions and constants) as JSON |
| `scripts/sync_shared.py` | JSON exports → `generated/` |

Card file names: lower case, dot becomes a dash (`Table.AddColumn` → `table-addcolumn`),
`#` becomes `hash-` (`#date` → `hash-date`).

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
python skills/m-reference/scripts/sync_shared.py exports/desktop.json exports/excel.json
python skills/m-reference/scripts/sync_shared.py exports/desktop.json exports/excel.json --write
```

The first export named wins each card; the rest only contribute `hosts`. Gates: an export
with fewer than 100 functions, two names mapping to one file, an orphan note, or the count
moving more than 5% (override with `--accept-count-change`). The new tree is built in a
scratch directory and swapped in one move.

## Related skills

- **`m-folding`** — whether a step folds to the source, and what breaks it.
- **`m-custom-functions`** — writing and documenting your own functions.
- **`m-iteration`** — `List.Generate`, `List.Accumulate`, buffering, pagination.
- **Modeling, partitions, TMDL, incremental refresh are not here.** Use the `power-query`
  skill from the [data-goblin plugin](https://github.com/data-goblin/power-bi-agentic-development).
