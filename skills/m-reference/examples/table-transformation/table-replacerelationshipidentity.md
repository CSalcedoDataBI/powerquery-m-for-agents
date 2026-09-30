<!-- lab: desktop 2.157.879.0 -->

# Table.ReplaceRelationshipIdentity

On a table built in memory, the table comes back unchanged.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ReplaceRelationshipIdentity(T, "id")
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
```
