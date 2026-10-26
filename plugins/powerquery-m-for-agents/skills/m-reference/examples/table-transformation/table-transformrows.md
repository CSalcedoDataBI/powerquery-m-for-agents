<!-- lab: desktop 2.157.879.0 -->

# Table.TransformRows

A list built from every row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.TransformRows(T, each [Name] & Text.From([Qty]))
```

```text
{"a1", "b2", "a3"}
```
