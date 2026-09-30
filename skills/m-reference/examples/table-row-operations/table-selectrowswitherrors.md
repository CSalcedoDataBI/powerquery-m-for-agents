<!-- lab: desktop 2.157.879.0 -->

# Table.SelectRowsWithErrors

Keep only the row whose conversion failed.

```m
Table.SelectRowsWithErrors(Table.TransformColumnTypes(#table({"v"}, {{"1"}, {"x"}}), {{"v", Int64.Type}}))
```

```text
#table(type table [v = nullable number], {{error: DataFormat.Error: We couldn't convert to Number. | Detail: "x"}})
```
