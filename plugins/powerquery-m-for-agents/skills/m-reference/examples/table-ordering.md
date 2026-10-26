<!-- lab: desktop 2.157.879.0 -->

# Executed examples: table-ordering

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Table.AddRankColumn

Dense ranking: ties share a rank and the next one is not skipped.

```m
Table.AddRankColumn(#table({"P", "S"}, {{"a", 10}, {"b", 20}, {"c", 20}}), "Rank", {"S", Order.Descending}, [RankKind = RankKind.Dense])
```

```text
#table(type table [P = any, S = any, Rank = nullable number], {{"b", 20, 1}, {"c", 20, 1}, {"a", 10, 2}})
```

## Table.Max

The row with the largest value.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Max(T, "Qty")
```

```text
[Name = "a", Qty = 3]
```

## Table.MaxN

The two rows with the largest values.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.MaxN(T, "Qty", 2)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 3}, {"b", 2}})
```

## Table.Min

The row with the smallest value.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Min(T, "Qty")
```

```text
[Name = "a", Qty = 1]
```

## Table.MinN

The two rows with the smallest values.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.MinN(T, "Qty", 2)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}})
```

## Table.Sort

Two sort keys.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Sort(T, {{"Name", Order.Ascending}, {"Qty", Order.Descending}})
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 3}, {"a", 1}, {"b", 2}})
```
