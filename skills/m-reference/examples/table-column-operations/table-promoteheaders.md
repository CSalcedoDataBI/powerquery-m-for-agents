<!-- lab: desktop 2.157.879.0 -->

# Table.PromoteHeaders

The first row becomes the headers.

```m
Table.PromoteHeaders(#table({"Column1", "Column2"}, {{"Name", "Qty"}, {"a", 1}}))
```

```text
#table(type table [Name = any, Qty = any], {{"a", 1}})
```
