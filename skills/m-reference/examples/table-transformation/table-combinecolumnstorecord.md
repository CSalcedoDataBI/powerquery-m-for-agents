<!-- lab: desktop 2.157.879.0 -->

# Table.CombineColumnsToRecord

Two columns into one record column.

```m
Table.CombineColumnsToRecord(#table({"a", "b"}, {{1, 2}}), "R", {"a", "b"})
```

```text
#table(type table [R = [a = any, b = any]], {{[a = 1, b = 2]}})
```
