<!-- lab: desktop 2.157.879.0 -->

# Table.View

A handler answers the row count instead of counting.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.RowCount(Table.View(T, [GetRowCount = () => 99]))
```

```text
99
```
