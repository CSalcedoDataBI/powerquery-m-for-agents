<!-- lab: desktop 2.157.879.0 -->

# Table.ExpandRecordColumn

Pick fields and name the new columns.

```m
Table.ExpandRecordColumn(#table({"r"}, {{[x = 1, y = 2]}}), "r", {"x"}, {"r.x"})
```

```text
#table(type table [#"r.x" = any], {{1}})
```
