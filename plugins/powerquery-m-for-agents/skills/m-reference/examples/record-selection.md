<!-- lab: desktop 2.157.879.0 -->

# Executed examples: record-selection

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Record.Field

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

## Record.FieldNames

Field names keep their source order, null values still count, case matters, and an empty record has no names.

```m
Record.FieldNames([B = null, A = 1])
```

```text
{"B", "A"}
```

```m
Record.FieldNames([a = 1, A = 2])
```

```text
{"a", "A"}
```

```m
Record.FieldNames([])
```

```text
{}
```

## Record.FieldOrDefault

These examples show what the optional default does when a field is missing, when it exists, and when its value is null.

```m
Record.FieldOrDefault([CustomerID = 1, Name = "Bob"], "Phone")
```

```text
null
```

```m
Record.FieldOrDefault([CustomerID = 1, Name = "Bob"], "Phone", "123-4567")
```

```text
"123-4567"
```

```m
Record.FieldOrDefault([CustomerID = 1, Phone = null], "Phone", "123-4567")
```

```text
null
```

## Record.FieldValues

Null field values are kept rather than dropped.

```m
Record.FieldValues([A = null, B = 2, C = null])
```

```text
{null, 2, null}
```

An empty record produces an empty list.

```m
Record.FieldValues([])
```

```text
{}
```

Nested records come back whole, not flattened.

```m
Record.FieldValues([A = [X = 1], B = 2])
```

```text
{[X = 1], 2}
```

## Record.SelectFields

These examples show how selection treats null values, a single text field name, and a field that is not present.

A null value is still a field value, so it survives selection.

```m
Record.SelectFields([A = 1, B = null, C = 3], {"B", "C"})
```

```text
[B = null, C = 3]
```

The `fields` argument accepts one text value as well as a list.

```m
Record.SelectFields([A = 1, B = 2], "B")
```

```text
[B = 2]
```

An absent field is kept as null when `missingField` is `MissingField.UseNull`.

```m
Record.SelectFields([A = 1, B = 2], {"A", "Z"}, MissingField.UseNull)
```

```text
[A = 1, Z = null]
```
