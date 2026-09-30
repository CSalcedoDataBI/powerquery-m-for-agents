<!-- lab: desktop 2.157.879.0 -->

# Table.Profile

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
