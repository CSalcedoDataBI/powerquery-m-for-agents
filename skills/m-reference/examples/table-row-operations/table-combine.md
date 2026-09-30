<!-- lab: desktop 2.157.879.0 -->

# Table.Combine

Columns are unioned; missing ones are null.

```m
Table.Combine({#table({"a"}, {{1}}), #table({"b"}, {{2}})})
```

```text
#table(type table [a = any, b = any], {{1, null}, {null, 2}})
```
