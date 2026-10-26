<!-- lab: desktop 2.157.879.0 -->

# Table.MinN

The two rows with the smallest values.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.MinN(T, "Qty", 2)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}})
```
