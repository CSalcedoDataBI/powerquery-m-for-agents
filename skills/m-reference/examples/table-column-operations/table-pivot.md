<!-- lab: desktop 2.157.879.0 -->

# Table.Pivot

Attribute values become columns.

```m
Table.Pivot(#table({"k", "attr", "v"}, {{"a", "x", 1}, {"a", "y", 2}, {"b", "x", 3}}), {"x", "y"}, "attr", "v")
```

```text
#table(type table [k = any, x = any, y = any], {{"a", 1, 2}, {"b", 3, null}})
```
