<!-- lab: desktop 2.157.879.0 -->

# Table.ExpandListColumn

One row per list item; an empty list leaves a null row.

```m
Table.ExpandListColumn(#table({"k", "v"}, {{"a", {1, 2}}, {"b", {}}}), "v")
```

```text
#table(type table [k = any, v = any], {{"a", 1}, {"a", 2}, {"b", null}})
```
