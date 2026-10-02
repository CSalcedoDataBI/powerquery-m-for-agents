# Probes

One-off investigations, each a script that runs in an already-open Power BI Desktop and records
what the engine returned. A probe's result is a measurement for one Desktop build, not a field
note; it becomes a note only once it reproduces.

## `casing_probe.ps1`: column-name casing between queries (#20)

The probe adds tables to the open model through TMSL, refreshes them in fixed groups and
orders, reads each one, and deletes them at the end. Each probe query reports three things:

- the column names `Table.ColumnNames` sees;
- whether a case-sensitive `List.Contains(..., "Name")` finds `Name`;
- what field access `T{0}[Name]` returns.

```bash
python lab/runner/run_examples.py --open    # one Desktop on the runner model; note its port
powershell.exe -NoProfile -File lab/probes/casing_probe.ps1 -Port <port> -Runs 20 -OutFile casing.json
```

**Result on Desktop 2.157.879.0 (2026-10-01): not reproduced.** It ran in two passes of 20
runs in one Desktop session: the first seven groups ran in both passes (40 times), and the
last three, added in the second pass, ran 20 times. That makes 600 table reads. There were no refresh errors, and every query
returned its own casing every time:

| Group (refreshed together, in this order) | Every run returned |
|---|---|
| `ProbeC` alone | `Name,Qty` |
| `ProbeF` + `ProbeC`, and `ProbeC` + `ProbeF` | `name,qty` and `Name,Qty` |
| `ProbeU` (`Table.TransformColumnNames(..., Text.Upper)`) + `ProbeC` | `NAME,QTY` and `Name,Qty` |
| `ProbeSlc` + `ProbeS` (typed tables parsed from text, no `#table` literal) | `name,qty` and `Name,Qty` |
| `ProbeF` + `ProbeLoadC` (loaded to the model as columns `Name`, `Qty`) | `name,qty`; the model rows `a 1`, `b 2`, `a 3` |
| `ProbeSame` (both literals in one query, lower case first) | `Name,Qty` |
| `ProbeEval` (both through `Expression.Evaluate`), alone and after `ProbeF` | `Name,Qty` |

What the checklist of #20 asked:

- **Repeated N times, with order and count recorded.** At least 20 runs of each group, in both
  orders for the pair: 0 leaks.
- **Does it reach the loaded model?** Not observed. `ProbeLoadC` loaded `Name` and `Qty`
  with their values while refreshed together with `ProbeF`.
- **Does it need `#table` literals?** Not observed with literals either. Typed tables
  parsed from text behaved the same.
- **Does case-sensitive logic break?** Not here. `List.Contains` found `Name` only in the
  tables whose own name is `Name`, and `T{0}[Name]` is an error on the lower-case tables:
  field access is case-sensitive.

The leak reported in #20 came from a different setup: blocks evaluated together by the
earlier runner. One refresh per block (`lab/runner/run_isolated.ps1`) stays, because it costs
little and removes the dependence either way. If the leak shows up again, rerun this probe
on that build and add the setup it came from as a new group.
