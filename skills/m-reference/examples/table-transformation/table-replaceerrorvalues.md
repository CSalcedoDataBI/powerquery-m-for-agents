<!-- lab: desktop 2.157.879.0 -->

# Table.ReplaceErrorValues

A failed conversion replaced by 0.

```m
Table.ReplaceErrorValues(Table.TransformColumnTypes(#table({"v"}, {{"1"}, {"x"}}), {{"v", Int64.Type}}), {{"v", 0}})
```

```text
#table(type table [v = nullable number], {{1}, {0}})
```
