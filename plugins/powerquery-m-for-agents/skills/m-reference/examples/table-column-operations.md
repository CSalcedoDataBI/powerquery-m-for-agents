<!-- lab: desktop 2.157.879.0 -->

# Executed examples: table-column-operations

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Table.Column

One column as a list.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Column(T, "Qty")
```

```text
{1, 2, 3}
```

## Table.ColumnNames

Names in order.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ColumnNames(T)
```

```text
{"Name", "Qty"}
```

## Table.ColumnsOfType

Columns whose type is text.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ColumnsOfType(T, {type text})
```

```text
{"Name"}
```

## Table.DemoteHeaders

Headers become the first row; types are lost.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.DemoteHeaders(T)
```

```text
#table(type table [Column1 = any, Column2 = any], {{"Name", "Qty"}, {"a", 1}, {"b", 2}, {"a", 3}})
```

## Table.DuplicateColumn

A copy keeps the type.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.DuplicateColumn(T, "Qty", "Qty2")
```

```text
#table(type table [Name = text, Qty = Int64.Type, Qty2 = Int64.Type], {{"a", 1, 1}, {"b", 2, 2}, {"a", 3, 3}})
```

## Table.HasColumns

One name, or all of a list.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.HasColumns(T, "Qty"), Table.HasColumns(T, {"Qty", "X"})}
```

```text
{true, false}
```

## Table.Pivot

Attribute values become columns.

```m
Table.Pivot(#table({"k", "attr", "v"}, {{"a", "x", 1}, {"a", "y", 2}, {"b", "x", 3}}), {"x", "y"}, "attr", "v")
```

```text
#table(type table [k = any, x = any, y = any], {{"a", 1, 2}, {"b", 3, null}})
```

## Table.PrefixColumns

Every column name gets the prefix and a dot.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ColumnNames(Table.PrefixColumns(T, "T"))
```

```text
{"T.Name", "T.Qty"}
```

## Table.PromoteHeaders

The first row becomes the headers.

```m
Table.PromoteHeaders(#table({"Column1", "Column2"}, {{"Name", "Qty"}, {"a", 1}}))
```

```text
#table(type table [Name = any, Qty = any], {{"a", 1}})
```

## Table.RemoveColumns

A missing column is an error unless told to ignore it.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.RemoveColumns(T, "Qty"), Table.RemoveColumns(T, "Nope", MissingField.Ignore), Table.RemoveColumns(T, "Nope")}
```

```text
{#table(type table [Name = text], {{"a"}, {"b"}, {"a"}}), #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}}), error: Expression.Error: The column 'Nope' of the table wasn't found. | Detail: "Nope"}
```

## Table.RenameColumns

Rename one column.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.RenameColumns(T, {{"Qty", "Quantity"}})
```

```text
#table(type table [Name = text, Quantity = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
```

## Table.ReorderColumns

Reorder columns.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ReorderColumns(T, {"Qty", "Name"})
```

```text
#table(type table [Qty = Int64.Type, Name = text], {{1, "a"}, {2, "b"}, {3, "a"}})
```

## Table.SelectColumns

Keep one column.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.SelectColumns(T, {"Qty"})
```

```text
#table(type table [Qty = Int64.Type], {{1}, {2}, {3}})
```

## Table.TransformColumnNames

Upper-case every column name.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.TransformColumnNames(T, Text.Upper)
```

```text
#table(type table [NAME = text, QTY = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
```

## Table.Unpivot

Listed columns become rows.

```m
Table.Unpivot(#table({"k", "x", "y"}, {{"a", 1, 2}}), {"x", "y"}, "Attr", "Val")
```

```text
#table(type table [k = any, Attr = text, Val = anynonnull], {{"a", "x", 1}, {"a", "y", 2}})
```

## Table.UnpivotOtherColumns

Every column but the key becomes rows.

```m
Table.UnpivotOtherColumns(#table({"k", "x", "y"}, {{"a", 1, 2}}), {"k"}, "Attr", "Val")
```

```text
#table(type table [k = any, Attr = text, Val = anynonnull], {{"a", "x", 1}, {"a", "y", 2}})
```
