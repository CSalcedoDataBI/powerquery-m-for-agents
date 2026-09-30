<!-- lab: desktop 2.157.879.0 -->

# Table.RowCount

Number of rows.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.RowCount(T)
```

```text
3
```
