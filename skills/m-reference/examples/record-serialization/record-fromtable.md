<!-- lab: desktop 2.157.879.0 -->

# Record.FromTable

A null value is kept as the field's value, an empty table gives an empty record, and duplicate field names raise an error.

```m
Record.FromTable(Table.FromRecords({[Name = "CustomerID", Value = 1], [Name = "Phone", Value = null]}))
```

```text
[CustomerID = 1, Phone = null]
```

```m
Record.FromTable(#table({"Name", "Value"}, {}))
```

```text
[]
```

```m
Record.FromTable(Table.FromRecords({[Name = "ID", Value = 1], [Name = "ID", Value = 2]}))
```

```text
error: Expression.Error: The field 'ID' already exists in the record. | Detail: [Name = "ID", Value = null]
```
