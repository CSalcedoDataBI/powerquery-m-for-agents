<!-- lab: desktop 2.157.879.0 -->

# Table.TransformColumns

Without a type, the column takes the declared return type of the function: Text.Upper declares nullable text.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Value.Type(Table.TransformColumns(T, {{"Name", Text.Upper}, {"Qty", each _ * 10, Int64.Type}}))
```

```text
type table [Name = nullable text, Qty = Int64.Type]
```
