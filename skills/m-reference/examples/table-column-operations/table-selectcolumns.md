<!-- lab: desktop 2.157.879.0 -->

# Table.SelectColumns

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
