<!-- lab: desktop 2.157.879.0 -->

# Executed examples: table-row-operations

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Table.AlternateRows

Keep the first row, then skip 1 and take 1.

```m
Table.AlternateRows(#table({"n"}, {{1}, {2}, {3}, {4}, {5}}), 1, 1, 1)
```

```text
#table(type table [n = any], {{1}, {3}, {5}})
```

## Table.Combine

Columns are unioned; missing ones are null.

```m
Table.Combine({#table({"a"}, {{1}}), #table({"b"}, {{2}})})
```

```text
#table(type table [a = any, b = any], {{1, null}, {null, 2}})
```

## Table.FindText

Rows where any cell contains the text.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.FindText(T, "b")
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"b", 2}})
```

## Table.First

The first row, or null when empty.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.First(T), Table.First(#table({"a"}, {}))}
```

```text
{[Name = "a", Qty = 1], null}
```

## Table.FirstN

A count, or a condition that stops at the first row failing it.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.FirstN(T, 2), Table.FirstN(T, each [Name] = "a")}
```

```text
{#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}}), #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}})}
```

## Table.FirstValue

The first cell of the first row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.FirstValue(T)
```

```text
"a"
```

## Table.FromPartitions

Tables stacked, each tagged with its partition value.

```m
Table.FromPartitions("Year", {{2023, #table({"v"}, {{1}})}, {2024, #table({"v"}, {{2}})}}, Int64.Type)
```

```text
#table(type table [v = any, Year = Int64.Type], {{1, 2023}, {2, 2024}})
```

## Table.InsertRows

Insert a row at position 1.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.InsertRows(T, 1, {[Name = "z", Qty = 9]})
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"z", 9}, {"b", 2}, {"a", 3}})
```

## Table.Last

The last row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Last(T)
```

```text
[Name = "a", Qty = 3]
```

## Table.LastN

The last rows.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.LastN(T, 2)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"b", 2}, {"a", 3}})
```

## Table.MatchesAllRows

Every row passes.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.MatchesAllRows(T, each [Qty] > 0)
```

```text
true
```

## Table.MatchesAnyRows

At least one row passes.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.MatchesAnyRows(T, each [Qty] > 2)
```

```text
true
```

## Table.Partition

Rows spread over two tables by a hash of the column.

```m
Table.Partition(#table({"n"}, {{1}, {2}, {3}, {4}}), "n", 2, each _)
```

```text
{#table(type table [n = any], {{2}, {4}}), #table(type table [n = any], {{1}, {3}})}
```

## Table.Range

One row from offset 1.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Range(T, 1, 1)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"b", 2}})
```

## Table.RemoveFirstN

Drop the first row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.RemoveFirstN(T, 1)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"b", 2}, {"a", 3}})
```

## Table.RemoveLastN

Drop the last row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.RemoveLastN(T, 1)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}})
```

## Table.RemoveRows

Remove two rows from the top.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.RemoveRows(T, 0, 2)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 3}})
```

## Table.RemoveRowsWithErrors

The row whose conversion failed is dropped.

```m
Table.RemoveRowsWithErrors(Table.TransformColumnTypes(#table({"v"}, {{"1"}, {"x"}}), {{"v", Int64.Type}}))
```

```text
#table(type table [v = nullable number], {{1}})
```

## Table.Repeat

The rows, three times.

```m
Table.Repeat(#table({"a"}, {{1}}), 3)
```

```text
#table(type table [a = any], {{1}, {1}, {1}})
```

## Table.ReplaceRows

Replace one row at the top.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ReplaceRows(T, 0, 1, {[Name = "z", Qty = 0]})
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"z", 0}, {"b", 2}, {"a", 3}})
```

## Table.ReverseRows

Rows in reverse order.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ReverseRows(T)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 3}, {"b", 2}, {"a", 1}})
```

## Table.SelectRows

Keep rows that pass.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.SelectRows(T, each [Qty] >= 2)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"b", 2}, {"a", 3}})
```

## Table.SelectRowsWithErrors

Keep only the row whose conversion failed.

```m
Table.SelectRowsWithErrors(Table.TransformColumnTypes(#table({"v"}, {{"1"}, {"x"}}), {{"v", Int64.Type}}))
```

```text
#table(type table [v = nullable number], {{error: DataFormat.Error: We couldn't convert to Number. | Detail: "x"}})
```

## Table.SingleRow

Exactly one row, or an error.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.SingleRow(#table({"a"}, {{1}})), Table.SingleRow(T)}
```

```text
{[a = 1], error: Expression.Error: There were too many elements in the enumeration to complete the operation. | Detail: {[Name = "a", Qty = 1], [Name = "b", Qty = 2], [Name = "a", Qty = 3]}}
```

## Table.Skip

Skip the first row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Skip(T, 1)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"b", 2}, {"a", 3}})
```

## Table.SplitAt

The first row, and the rest.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.SplitAt(T, 1)
```

```text
{#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}}), #table(type table [Name = text, Qty = Int64.Type], {{"b", 2}, {"a", 3}})}
```
