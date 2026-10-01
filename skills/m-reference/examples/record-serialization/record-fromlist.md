<!-- lab: desktop 2.157.879.0 -->

# Record.FromList

Nulls are ordinary values, a record type supplies only field names and order, and duplicate field names are rejected.

```m
Record.FromList({null, "Bob"}, {"CustomerID", "Name"})
```

```text
[CustomerID = null, Name = "Bob"]
```

A record type does not convert the list values to the declared types.

```m
Record.FromList({"123-4567", 1}, type [Phone = number, CustomerID = text])
```

```text
[Phone = "123-4567", CustomerID = 1]
```

Duplicate field names are an error even when the values are valid.

```m
Record.FromList({1, 2}, {"ID", "ID"})
```

```text
error: Expression.Error: The field 'ID' already exists in the record. | Detail: [Name = "ID", Value = null]
```
