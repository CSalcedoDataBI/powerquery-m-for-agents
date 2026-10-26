<!-- lab: desktop 2.157.879.0 -->

# Table.ToRows

One list per row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ToRows(T)
```

```text
{{"a", 1}, {"b", 2}, {"a", 3}}
```
