<!-- lab: desktop 2.157.879.0 -->

# Table.RemoveMatchingRows

Remove rows matching on one column.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.RemoveMatchingRows(T, {[Name = "a"]}, "Name")
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"b", 2}})
```
