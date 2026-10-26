<!-- lab: desktop 2.157.879.0 -->

# Table.ReverseRows

Rows in reverse order.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ReverseRows(T)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 3}, {"b", 2}, {"a", 1}})
```
