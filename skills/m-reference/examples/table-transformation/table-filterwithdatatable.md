<!-- lab: desktop 2.157.879.0 -->

# Table.FilterWithDataTable

Called on a table built in memory, the identifier is looked up as a variable.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.FilterWithDataTable(T, "x")
```

```text
error: Expression.Error: The variable 'x' could not be found.
```
