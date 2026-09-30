<!-- lab: desktop 2.157.879.0 -->

# Table.ToColumns

One list per column.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ToColumns(T)
```

```text
{{"a", "b", "a"}, {1, 2, 3}}
```
