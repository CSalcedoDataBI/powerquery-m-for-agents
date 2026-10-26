<!-- lab: desktop 2.157.879.0 -->

# Table.InsertRows

Insert a row at position 1.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.InsertRows(T, 1, {[Name = "z", Qty = 9]})
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"z", 9}, {"b", 2}, {"a", 3}})
```
