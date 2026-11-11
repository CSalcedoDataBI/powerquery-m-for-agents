<!-- lab: desktop 2.159.883.0 -->

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

## Tables.GetRelationships

All three calls fail, each on an in-memory table: with a `Data` column, with a differently named column passed as `dataColumn`, and with no `Data` column at all.

```m
Tables.GetRelationships(
    #table({"Name", "Data"}, {
        {"Orders", Table.AddKey(#table({"OrderID", "CustomerID"}, {{1, 10}, {2, 20}}), {"OrderID"}, true)},
        {"Customers", Table.AddKey(#table({"CustomerID", "City"}, {{10, "Seattle"}, {20, "Redmond"}}), {"CustomerID"}, true)}
    })
)
```

```text
error: Expression.Error: The argument value isn't valid. | Detail: "dataColumn"
```

```m
Tables.GetRelationships(
    #table({"Name", "Tbl"}, {
        {"Orders", Table.AddKey(#table({"OrderID", "CustomerID"}, {{1, 10}}), {"OrderID"}, true)},
        {"Customers", Table.AddKey(#table({"CustomerID", "City"}, {{10, "Seattle"}}), {"CustomerID"}, true)}
    }),
    "Tbl"
)
```

```text
error: Expression.Error: We can't get the relationships. A primary or unique key is required to perform the operation against the table.
```

```m
Tables.GetRelationships(
    #table({"Name", "Tbl"}, {
        {"Orders", #table({"OrderID"}, {{1}})}
    })
)
```

```text
error: Expression.Error: The argument value isn't valid. | Detail: "dataColumn"
```
