<!-- lab: desktop 2.157.879.0 -->

# Table.ReplacePartitionKey

Set the partition key, then read it back.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.PartitionKey(Table.ReplacePartitionKey(T, {"Name"}))
```

```text
{"Name"}
```
