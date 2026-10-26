<!-- lab: desktop 2.157.879.0 -->

# Table.Column

One column as a list.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Column(T, "Qty")
```

```text
{1, 2, 3}
```
