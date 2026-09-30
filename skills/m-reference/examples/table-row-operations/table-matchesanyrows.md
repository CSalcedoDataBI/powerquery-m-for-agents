<!-- lab: desktop 2.157.879.0 -->

# Table.MatchesAnyRows

At least one row passes.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.MatchesAnyRows(T, each [Qty] > 2)
```

```text
true
```
