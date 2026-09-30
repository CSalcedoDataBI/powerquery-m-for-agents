<!-- lab: desktop 2.157.879.0 -->

# Table.DuplicateColumn

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
