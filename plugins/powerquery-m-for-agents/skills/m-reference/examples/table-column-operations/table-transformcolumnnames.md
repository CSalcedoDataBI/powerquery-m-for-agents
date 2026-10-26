<!-- lab: desktop 2.157.879.0 -->

# Table.TransformColumnNames

Upper-case every column name.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.TransformColumnNames(T, Text.Upper)
```

```text
#table(type table [NAME = text, QTY = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
```
