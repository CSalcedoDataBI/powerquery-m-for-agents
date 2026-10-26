<!-- lab: desktop 2.157.879.0 -->

# Executed examples: table-conversions

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Table.ToColumns

One list per column.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ToColumns(T)
```

```text
{{"a", "b", "a"}, {1, 2, 3}}
```

## Table.ToList

Each row combined into one text.

```m
Table.ToList(#table({"a", "b"}, {{"x", "y"}, {"z", "w"}}), Combiner.CombineTextByDelimiter("|"))
```

```text
{"x|y", "z|w"}
```

## Table.ToRecords

One record per row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ToRecords(T)
```

```text
{[Name = "a", Qty = 1], [Name = "b", Qty = 2], [Name = "a", Qty = 3]}
```

## Table.ToRows

One list per row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ToRows(T)
```

```text
{{"a", 1}, {"b", 2}, {"a", 3}}
```
