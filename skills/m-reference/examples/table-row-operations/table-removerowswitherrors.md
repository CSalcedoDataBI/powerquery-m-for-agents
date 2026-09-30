<!-- lab: desktop 2.157.879.0 -->

# Table.RemoveRowsWithErrors

The row whose conversion failed is dropped.

```m
Table.RemoveRowsWithErrors(Table.TransformColumnTypes(#table({"v"}, {{"1"}, {"x"}}), {{"v", Int64.Type}}))
```

```text
#table(type table [v = nullable number], {{1}})
```
