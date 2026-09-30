<!-- lab: desktop 2.157.879.0 -->

# Table.Range

One row from offset 1.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Range(T, 1, 1)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"b", 2}})
```
