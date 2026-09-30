<!-- lab: desktop 2.157.879.0 -->

# Table.Min

The row with the smallest value.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Min(T, "Qty")
```

```text
[Name = "a", Qty = 1]
```
