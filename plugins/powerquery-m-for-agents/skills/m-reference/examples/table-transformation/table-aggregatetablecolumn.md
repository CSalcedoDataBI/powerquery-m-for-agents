<!-- lab: desktop 2.157.879.0 -->

# Table.AggregateTableColumn

Aggregate a nested table column into a new column.

```m
Table.AggregateTableColumn(#table({"G", "T"}, {{"x", #table({"v"}, {{1}, {2}})}}), "T", {{"v", List.Sum, "Total"}})
```

```text
#table(type table [G = any, Total = any], {{"x", 3}})
```
