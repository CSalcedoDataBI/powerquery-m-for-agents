<!-- lab: desktop 2.157.879.0 -->

# Table.UnpivotOtherColumns

Every column but the key becomes rows.

```m
Table.UnpivotOtherColumns(#table({"k", "x", "y"}, {{"a", 1, 2}}), {"k"}, "Attr", "Val")
```

```text
#table(type table [k = any, Attr = text, Val = any], {{"a", "x", 1}, {"a", "y", 2}})
```
