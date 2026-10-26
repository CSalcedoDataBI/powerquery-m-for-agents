<!-- lab: desktop 2.157.879.0 -->

# Executed examples: table-membership

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Table.Contains

A partial record matches on the fields it has.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Contains(T, [Name = "b"])
```

```text
true
```

## Table.ContainsAll

Every row must be found.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ContainsAll(T, {[Name = "a"], [Name = "z"]})
```

```text
false
```

## Table.ContainsAny

One row is enough.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ContainsAny(T, {[Name = "z"], [Qty = 2]})
```

```text
true
```

## Table.Distinct

Distinct on one column keeps one row per value.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Distinct(T, {"Name"})
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}})
```

## Table.IsDistinct

Distinct on one column.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.IsDistinct(T, {"Name"})
```

```text
false
```

## Table.PositionOf

The position of a whole row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.PositionOf(T, [Name = "a", Qty = 3])
```

```text
2
```

## Table.PositionOfAny

The first position of any of the rows.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.PositionOfAny(T, {[Name = "b", Qty = 2]})
```

```text
1
```

## Table.RemoveMatchingRows

Remove rows matching on one column.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.RemoveMatchingRows(T, {[Name = "a"]}, "Name")
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"b", 2}})
```

## Table.ReplaceMatchingRows

Replace whole rows by value.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ReplaceMatchingRows(T, {{[Name = "b", Qty = 2], [Name = "B", Qty = 20]}})
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"B", 20}, {"a", 3}})
```
