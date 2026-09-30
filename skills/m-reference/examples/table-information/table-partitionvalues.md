<!-- lab: desktop 2.157.879.0 -->

# Table.PartitionValues

On a table that is not partitioned: one row, no columns.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.PartitionValues(T)
```

```text
#table(type table [], {{}})
```
