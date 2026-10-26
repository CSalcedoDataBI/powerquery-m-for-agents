<!-- lab: desktop 2.157.879.0 -->

# Table.Sort

Two sort keys.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Sort(T, {{"Name", Order.Ascending}, {"Qty", Order.Descending}})
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 3}, {"a", 1}, {"b", 2}})
```
