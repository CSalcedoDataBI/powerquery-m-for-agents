<!-- lab: desktop 2.157.879.0 -->

# Executed examples: table-information

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Table.ApproximateRowCount

On an in-memory table.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ApproximateRowCount(T)
```

```text
3
```

## Table.ColumnCount

Number of columns.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ColumnCount(T)
```

```text
2
```

## Table.IsEmpty

Empty or not.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.IsEmpty(T), Table.IsEmpty(Table.FirstN(T, 0))}
```

```text
{false, true}
```

## Table.PartitionValues

On a table that is not partitioned: one row, no columns.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.PartitionValues(T)
```

```text
#table(type table [], {{}})
```

## Table.Profile

Statistics per column (a few of the columns shown).

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.SelectColumns(Table.Profile(T), {"Column", "Min", "Max", "Count", "DistinctCount"})
```

```text
#table(type table [Column = Text.Type, Min = any, Max = any, Count = number, DistinctCount = any], {{"Name", "a", "b", 3, 2}, {"Qty", 1, 3, 3, 3}})
```

## Table.RowCount

Number of rows.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.RowCount(T)
```

```text
3
```

## Table.Schema

Column metadata (a few of its columns shown).

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.SelectColumns(Table.Schema(T), {"Name", "Position", "TypeName", "Kind"})
```

```text
#table(type table [Name = text, Position = number, TypeName = text, Kind = text], {{"Name", 0, "Text.Type", "text"}, {"Qty", 1, "Int64.Type", "number"}})
```
