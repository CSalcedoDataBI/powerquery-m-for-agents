<!-- lab: desktop 2.157.879.0 -->

# Record.RemoveFields

A null value is still a present field, but removing an absent field name raises an error unless the optional argument ignores it.

```m
Record.RemoveFields([A = null, B = 1], "A")
```

```text
[B = 1]
```

```m
Record.RemoveFields([A = 1, B = 2], "C")
```

```text
error: Expression.Error: The field 'C' of the record wasn't found. | Detail: [A = 1, B = 2]
```

```m
Record.RemoveFields([A = 1, B = 2], {"B", "C"}, MissingField.Ignore)
```

```text
[A = 1]
```
