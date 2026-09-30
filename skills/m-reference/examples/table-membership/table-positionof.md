<!-- lab: desktop 2.157.879.0 -->

# Table.PositionOf

The position of a whole row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.PositionOf(T, [Name = "a", Qty = 3])
```

```text
2
```
