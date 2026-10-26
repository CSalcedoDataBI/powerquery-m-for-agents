<!-- lab: desktop 2.157.879.0 -->

# Record.FieldValues

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
