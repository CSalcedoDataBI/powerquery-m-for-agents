<!-- lab: desktop 2.157.879.0 -->

# Table.ContainsAny

One row is enough.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ContainsAny(T, {[Name = "z"], [Qty = 2]})
```

```text
true
```
