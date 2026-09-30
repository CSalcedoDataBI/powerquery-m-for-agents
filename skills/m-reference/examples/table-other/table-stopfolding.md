<!-- lab: desktop 2.157.879.0 -->

# Table.StopFolding

On an in-memory table there is nothing to fold.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.StopFolding(T)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
```
