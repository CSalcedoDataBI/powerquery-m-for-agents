<!-- lab: desktop 2.157.879.0 -->

# Table.FillDown

Nulls take the value above.

```m
Table.FillDown(#table({"G", "v"}, {{"a", 1}, {null, 2}, {"b", 3}}), {"G"})
```

```text
#table(type table [G = any, v = any], {{"a", 1}, {"a", 2}, {"b", 3}})
```
