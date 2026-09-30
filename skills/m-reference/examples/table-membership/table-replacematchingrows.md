<!-- lab: desktop 2.157.879.0 -->

# Table.ReplaceMatchingRows

Replace whole rows by value.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ReplaceMatchingRows(T, {{[Name = "b", Qty = 2], [Name = "B", Qty = 20]}})
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"B", 20}, {"a", 3}})
```
