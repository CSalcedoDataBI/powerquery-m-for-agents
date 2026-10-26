<!-- lab: desktop 2.157.879.0 -->

# Table.Distinct

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
