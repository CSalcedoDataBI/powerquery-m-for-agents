<!-- lab: desktop 2.157.879.0 -->

# Table.ExpandTableColumn

One row per nested row.

```m
Table.ExpandTableColumn(#table({"k", "t"}, {{"a", #table({"v"}, {{1}, {2}})}}), "t", {"v"})
```

```text
#table(type table [k = any, v = any], {{"a", 1}, {"a", 2}})
```
