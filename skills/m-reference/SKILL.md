---
name: m-reference
description: Use when you need to know whether a Power Query M library function exists, its exact signature and parameter types, what it returns, which hosts have it (Power BI Desktop, Excel, Dataflows Gen2), or which of several similar functions to reach for — and for the M language itself when no single function is in question, such as let/in, each and the underscore, records, lists and tables, types and metadata, try/otherwise/catch, lazy evaluation and streaming. Triggers on "what does X do in M", "Power Query function signature", "is there an M function to", "Table.Join vs Table.NestedJoin", "does X exist in Excel Power Query", "M syntax", "each _", "try otherwise", "Power Query types".
---

# M Reference

Every Power Query M library function, agent-native. The catalogue is **exported from the
engine itself** (`#shared`), not scraped from documentation: a function in the catalogue
exists in the host it names. See
[the design spec](../../docs/superpowers/specs/2026-09-28-powerquery-m-for-agents-design.md).

> **Status.** `generated/` is built from one export: Power BI Desktop (the host and build are
> in the header of `catalog.md`). No other host yet, so no card carries ⌂. Which functions
> have executed examples is the ▶ flag in `catalog.md`.

## How to use this

**A question about the language itself** - `let`/`in`, `each` and `_`, records, lists and
tables, types, `try`/`otherwise`/`catch`, laziness - no function answers. Read
**`concepts.md`** and open the one page it points to.

**A question about a function. One hop. Do not read the whole library.**

1. **Search** **`generated/catalog.md`** for the name or its prefix (`Table.Join`, `Text.`);
   do not read it whole. Every library function has one row: name, category, return type,
   flags, one-line summary. Looking for a connector (`Snowflake.Databases`,
   `Stripe.Contents`)? Search **`generated/connectors.md`** instead. A constant or type value
   (`JoinKind.Inner`, `Int64.Type`)? **`generated/constants.md`**, which already holds the
   whole answer: there are no constant cards.
2. Find the function. Open its card: **`generated/library/<file>.md`** (file naming below).
   Connector cards live there too.
3. Flag **★** → also read **`notes/<file>.md`**: field knowledge not in the engine metadata,
   each claim next to the query that shows it.
4. Flag **▶** → the card links to **`examples/<category>/<file>.md`**: queries executed in
   this repository's lab, each with the value the engine returned. Prefer these over the
   card's own `## Examples` section, whose stated results nobody ran.
5. Flag **⌂** → the function is missing from at least one exported host. The card says
   which ones have it. Check before suggesting it for Excel or a dataflow.

In `concepts/`, `notes/` and `examples/`, the ```` ```text ```` block after each ```` ```m ````
block is what the engine returned, written by the lab runner, never typed. Results are M
literals; an error shows as `error: <Reason>: <Message>`.

**A name that matches none of `catalog.md`, `connectors.md` and `constants.md` does not exist
in any exported host.** Say so rather than offering it. That covers functions, connector
entry points and constants such as `GroupKind.Local` or `Occurrence.All`. One kind of name is
**not** covered, so its absence proves nothing:

- **Literal keywords** such as `#date`, `#table`, `#duration`. They are part of the language
  syntax, not library members.

A connector is a function the engine gives no category, under a prefix no library function
uses. Many carry no description. Data-access functions the engine documents (`Csv.Document`,
`Web.Contents`, `Sql.Database`, …) are library, in `catalog.md`.

## Layout

| Path | What it is |
|---|---|
| `generated/catalog.md` | The index the agent reads: library functions. **Generated** |
| `generated/connectors.md` | Connector entry points, same columns. **Generated** |
| `generated/constants.md` | Constants and type values, with their value. **Generated** |
| `generated/catalog/` | All three indexes for scripts, one JSON file per category root. **Generated**, never loaded into context |
| `generated/library/<file>.md` | One card per function or connector. **Generated — never edit by hand** |
| `concepts.md` | Index of the language pages. **Hand-written** |
| `concepts/<topic>.md` | One page per language topic, with executed blocks. **Hand-written** |
| `notes/<file>.md` | Field notes. **Hand-written**; the sync never touches them |
| `examples/<category>/<file>.md` | Executed examples. **Hand-written** code; results written by the lab runner |
| `scripts/export_shared.pq` | The M query that dumps `#shared` (functions and constants) as JSON |
| `scripts/sync_shared.py` | JSON exports → `generated/` |

Card file names: lower case, every run of non-alphanumerics becomes one dash
(`Table.AddColumn` → `table-addcolumn`); a leading `#` would become `hash-`, though no
exported name starts with one.

Regenerating `generated/` or running the lab is maintainer work, in
[MAINTAINING.md](MAINTAINING.md). Answering a question about M never needs it.

## Related skills

- **Modeling, partitions, TMDL, incremental refresh are not here.** Use the `power-query`
  skill from the [data-goblin plugin](https://github.com/data-goblin/power-bi-agentic-development).
