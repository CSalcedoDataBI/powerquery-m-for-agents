<!-- lab: desktop 2.157.879.0 -->

# Table.HasColumns

One name, or all of a list.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.HasColumns(T, "Qty"), Table.HasColumns(T, {"Qty", "X"})}
```

```text
{true, false}
```
