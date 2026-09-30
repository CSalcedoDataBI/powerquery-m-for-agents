<!-- lab: desktop 2.157.879.0 -->

# Table.AddColumn

With the fourth argument the column is typed; without it, it is any.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Value.Type(Table.AddColumn(T, "D", each [Qty] * 2, Int64.Type)), Value.Type(Table.AddColumn(T, "D", each [Qty] * 2))}
```

```text
{type table [Name = text, Qty = Int64.Type, D = Int64.Type], type table [Name = text, Qty = Int64.Type, D = any]}
```
