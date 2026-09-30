<!-- lab: desktop 2.157.879.0 -->

# Table.TransformColumnTypes: errors that wait for the cell

A value that does not convert becomes an error in its cell. The step itself succeeds: `try`
on the table reports no error and the row count is right. The failure only shows when that
cell is read - in Power BI, during refresh.

```m
let
    T = Table.TransformColumnTypes(#table({"v"}, {{"1"}, {"x"}}), {{"v", Int64.Type}})
in
    {(try T)[HasError], Table.RowCount(T), T{1}}
```

```text
{false, 2, [v = error: DataFormat.Error: We couldn't convert to Number. | Detail: "x"]}
```

The culture changes what converts, silently: `"1.5"` read as es-ES is fifteen.

```m
{Table.TransformColumnTypes(#table({"n"}, {{"1.5"}}), {{"n", type number}}, "en-US"), Table.TransformColumnTypes(#table({"n"}, {{"1.5"}}), {{"n", type number}}, "es-ES")}
```

```text
{#table(type table [n = nullable number], {{1.5}}), #table(type table [n = nullable number], {{15}})}
```

**Do this:** pass the culture of the data as the third argument, and after converting, check
for error cells before loading - `Table.SelectRowsWithErrors` lists them,
`Table.RemoveRowsWithErrors` or `Table.ReplaceErrorValues` handle them.
