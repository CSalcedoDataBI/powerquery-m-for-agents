<!-- lab: desktop 2.157.879.0 -->

# Table.RenameColumns

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
