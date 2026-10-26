<!-- lab: desktop 2.157.879.0 -->

# Table.ColumnsOfType

Columns whose type is text.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ColumnsOfType(T, {type text})
```

```text
{"Name"}
```
