<!-- lab: desktop 2.157.879.0 -->

# Table.PositionOfAny

The first position of any of the rows.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.PositionOfAny(T, {[Name = "b", Qty = 2]})
```

```text
1
```
