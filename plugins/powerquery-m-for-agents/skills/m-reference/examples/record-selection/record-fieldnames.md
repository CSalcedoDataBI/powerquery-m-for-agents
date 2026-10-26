<!-- lab: desktop 2.157.879.0 -->

# Record.FieldNames

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
