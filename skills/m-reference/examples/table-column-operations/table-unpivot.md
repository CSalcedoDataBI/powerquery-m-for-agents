<!-- lab: desktop 2.157.879.0 -->

# Table.Unpivot

Listed columns become rows.

```m
Table.Unpivot(#table({"k", "x", "y"}, {{"a", 1, 2}}), {"x", "y"}, "Attr", "Val")
```

```text
#table(type table [k = any, Attr = text, Val = any], {{"a", "x", 1}, {"a", "y", 2}})
```
