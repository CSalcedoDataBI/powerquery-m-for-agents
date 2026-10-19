<!-- lab: desktop 2.158.1304.0 -->

# Table.NestedJoin: buffer a right side that reads a source

**What happens:** each row of a nested join holds its own nested table, a view over the right
side. When every row reads it - `Table.IsEmpty([m])` to flag a match, `Table.RowCount([m])` -
and the right side is a query that reads files or other queries, its cost can be paid again
row by row. A case reported from another project's lab (1,242 rows on the left, a right side
derived from a query with five joins over files) took 172.8 s; with `Table.Buffer` on the right
side, 3.8 s, with the same result.

Buffering does not change what the join returns:

```m
let
    Left = Table.FromList({1..2000}, Splitter.SplitByNothing(), {"k"}),
    Right = Table.Distinct(Table.FromList(List.Transform({1..2000}, each Number.Mod(_, 500)), Splitter.SplitByNothing(), {"k"})),
    Flag = (r) => Table.AddColumn(Table.NestedJoin(Left, {"k"}, r, {"k"}, "m", JoinKind.LeftOuter), "found", each not Table.IsEmpty([m]))
in
    {List.Count(List.Select(Flag(Right)[found], each _)), Flag(Right)[found] = Flag(Table.Buffer(Right))[found]}
```

```text
{499, true}
```

**What this lab did not see:** with a right side built from literals, as above, there was no
difference to measure: 200 rows against a right side distilled from 200,000 values ran in
under a second with and without `Table.Buffer` (Power BI Desktop, 2026-10-19). Within one
evaluation the engine reads such a right side once. The cost belongs to a right side that goes
back to its source, so the block above proves the result is unchanged, not the timing.

**Do this:** when the rows of a nested join read their nested table, put the right side in
memory first: `Right = Table.Buffer(...)` (or `List.Buffer` for a list looked up row by row).
It is safe for the result; it costs the memory of the right side.
