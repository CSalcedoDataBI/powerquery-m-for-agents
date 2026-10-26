<!-- lab: desktop 2.157.879.0 -->

# Table.DemoteHeaders

Headers become the first row; types are lost.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.DemoteHeaders(T)
```

```text
#table(type table [Column1 = any, Column2 = any], {{"Name", "Qty"}, {"a", 1}, {"b", 2}, {"a", 3}})
```
