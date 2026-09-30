# Lab

Everything here runs Power Query M in Power BI Desktop's own engine, so the pages can quote
what the engine returned instead of what we expect. No external sources: data comes from
`#table` literals.

| Folder | What it runs |
|---|---|
| `shared-export/` | `export_shared.pq` in a generated PBIP, to export `#shared` → `exports/*.json` |
| `runner/` | Every ```` ```m ```` block under `skills/`, writing each result below its block |
| `drafting/` | A pilot (#21): an outside model drafts example pages in a container; the runner decides what they return |

## The runner

`run_examples.py` gathers the blocks into `runner.pq`, which renders any value as an M literal
(tables with their column types, errors as `error: <Reason>: <Message>`). A throwaway PBIP in
`runner/build/` (ignored by git) has one partition that reads that query from a file and
evaluates it with `Expression.Evaluate` over `#shared`.

```bash
python lab/runner/run_examples.py --open                 # once: opens Desktop, leaves it open
python lab/runner/run_examples.py --port <port> --write  # every block, each in its own refresh
python lab/runner/run_examples.py --port <port> --check  # exit 1 if any written result changed
```

Each block runs in its **own refresh**. Evaluated together in one refresh, blocks leaked into
each other: a table type from one block showed up in another block that used the same
`#table` literal with different column-name casing (2026-09-29). One refresh per block
removes that dependence; two full runs then return identical results.

Without `--port`, a run opens and closes its own Desktop and evaluates everything in one
refresh: fine for a quick look, and it refuses `--write`/`--check` unless `--allow-batch`
says so on purpose.

`--only <text>[,<text>]` limits a run to the pages whose path contains any of the texts.

The runner refuses a block that could reach outside the engine - `#shared`, a data source, a
connector, `Expression.Evaluate` - before anything runs: every block is code evaluated on the
machine that runs it, and on a public repo a page can come from anyone. Values that only
describe that machine (`DateTimeZone.LocalNow`, `Culture.Current`, ...) are refused too.
Not every one can be caught by name: a conversion from `datetime` to `datetimezone` takes the
machine's zone. Check a result's `#datetimezone` offsets before committing it. Culture is not one of these:
the runner's model sets `culture` and `sourceQueryCulture` to en-US, so a conversion without
an explicit culture reads en-US on any machine.
