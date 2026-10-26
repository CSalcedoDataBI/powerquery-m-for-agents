<!-- lab: desktop 2.157.879.0 -->

# Table.PartitionKey

A table built in memory has no partition key.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.PartitionKey(T)
```

```text
null
```
