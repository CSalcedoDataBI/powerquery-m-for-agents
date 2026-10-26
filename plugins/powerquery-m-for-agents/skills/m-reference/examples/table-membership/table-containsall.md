<!-- lab: desktop 2.157.879.0 -->

# Table.ContainsAll

Every row must be found.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ContainsAll(T, {[Name = "a"], [Name = "z"]})
```

```text
false
```
