<!-- lab: desktop 2.157.879.0 -->

# Table.Skip

Skip the first row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Skip(T, 1)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"b", 2}, {"a", 3}})
```
