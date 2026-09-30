<!-- lab: desktop 2.157.879.0 -->

# Table.ReorderColumns

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
