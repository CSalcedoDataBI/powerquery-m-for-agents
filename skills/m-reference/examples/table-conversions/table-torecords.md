<!-- lab: desktop 2.157.879.0 -->

# Table.ToRecords

One record per row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ToRecords(T)
```

```text
{[Name = "a", Qty = 1], [Name = "b", Qty = 2], [Name = "a", Qty = 3]}
```
