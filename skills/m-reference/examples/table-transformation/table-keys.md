<!-- lab: desktop 2.157.879.0 -->

# Table.Keys

A table built in memory has no keys.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Keys(T)
```

```text
{}
```
