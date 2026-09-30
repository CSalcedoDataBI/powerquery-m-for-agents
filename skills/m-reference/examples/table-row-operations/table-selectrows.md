<!-- lab: desktop 2.157.879.0 -->

# Table.SelectRows

Keep rows that pass.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.SelectRows(T, each [Qty] >= 2)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"b", 2}, {"a", 3}})
```
