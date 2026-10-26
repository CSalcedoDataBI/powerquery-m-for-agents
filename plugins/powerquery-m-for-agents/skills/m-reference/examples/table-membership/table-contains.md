<!-- lab: desktop 2.157.879.0 -->

# Table.Contains

A partial record matches on the fields it has.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Contains(T, [Name = "b"])
```

```text
true
```
