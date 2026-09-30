<!-- lab: desktop 2.157.879.0 -->

# Table.Group

Sum per key.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Group(T, {"Name"}, {{"Total", each List.Sum([Qty]), Int64.Type}})
```

```text
#table(type table [Name = text, Total = Int64.Type], {{"a", 4}, {"b", 2}})
```
