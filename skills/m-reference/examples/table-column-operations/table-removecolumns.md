<!-- lab: desktop 2.157.879.0 -->

# Table.RemoveColumns

A missing column is an error unless told to ignore it.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.RemoveColumns(T, "Qty"), Table.RemoveColumns(T, "Nope", MissingField.Ignore), Table.RemoveColumns(T, "Nope")}
```

```text
{#table(type table [Name = text], {{"a"}, {"b"}, {"a"}}), #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}}), error: Expression.Error: The column 'Nope' of the table wasn't found. | Detail: "Nope"}
```
