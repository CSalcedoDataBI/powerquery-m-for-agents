<!-- lab: desktop 2.157.879.0 -->

# Table.MaxN

The two rows with the largest values.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.MaxN(T, "Qty", 2)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 3}, {"b", 2}})
```
