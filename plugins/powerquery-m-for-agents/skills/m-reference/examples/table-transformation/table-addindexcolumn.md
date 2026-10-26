<!-- lab: desktop 2.157.879.0 -->

# Table.AddIndexColumn

An index from 1.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.AddIndexColumn(T, "Index", 1, 1, Int64.Type)
```

```text
#table(type table [Name = text, Qty = Int64.Type, Index = Int64.Type], {{"a", 1, 1}, {"b", 2, 2}, {"a", 3, 3}})
```
