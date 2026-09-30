<!-- lab: desktop 2.157.879.0 -->

# Table.FillUp

Nulls take the value below.

```m
Table.FillUp(#table({"G", "v"}, {{null, 1}, {"a", 2}}), {"G"})
```

```text
#table(type table [G = any, v = any], {{"a", 1}, {"a", 2}})
```
