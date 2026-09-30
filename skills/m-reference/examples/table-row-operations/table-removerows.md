<!-- lab: desktop 2.157.879.0 -->

# Table.RemoveRows

Remove two rows from the top.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.RemoveRows(T, 0, 2)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 3}})
```
