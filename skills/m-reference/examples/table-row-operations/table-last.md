<!-- lab: desktop 2.157.879.0 -->

# Table.Last

The last row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Last(T)
```

```text
[Name = "a", Qty = 3]
```
