<!-- lab: desktop 2.157.879.0 -->

# Record.SelectFields

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
