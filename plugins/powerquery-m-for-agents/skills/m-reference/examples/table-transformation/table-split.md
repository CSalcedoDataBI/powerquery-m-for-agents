<!-- lab: desktop 2.157.879.0 -->

# Table.Split

Pages of two rows.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Split(T, 2)
```

```text
{#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}}), #table(type table [Name = text, Qty = Int64.Type], {{"a", 3}})}
```
