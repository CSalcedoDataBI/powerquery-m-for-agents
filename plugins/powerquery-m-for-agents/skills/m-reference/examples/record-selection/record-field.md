<!-- lab: desktop 2.157.879.0 -->

# Record.Field

A field whose value is null returns null, while a field name that does not exist raises an error.

```m
Record.Field([Name = "Bob", Phone = null], "Phone")
```

```text
null
```

```m
Record.Field([Name = "Bob"], "Phone")
```

```text
error: Expression.Error: The field 'Phone' of the record wasn't found. | Detail: [Name = "Bob"]
```

A field can itself hold a record, which is returned whole.

```m
Record.Field([CustomerID = 1, Address = [City = "Seattle", Zip = "98001"]], "Address")
```

```text
[City = "Seattle", Zip = "98001"]
```
