<!-- lab: desktop 2.157.879.0 -->

# Table.ReplaceRows

Replace one row at the top.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ReplaceRows(T, 0, 1, {[Name = "z", Qty = 0]})
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"z", 0}, {"b", 2}, {"a", 3}})
```
