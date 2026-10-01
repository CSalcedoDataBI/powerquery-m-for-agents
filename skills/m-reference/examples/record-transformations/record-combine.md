<!-- lab: desktop 2.157.879.0 -->

# Record.Combine

Nulls survive the combine and edge-case lists still produce a record.

```m
Record.Combine({[A = 1, B = null], [C = null]})
```

```text
[A = 1, B = null, C = null]
```

An empty list of records gives an empty record.

```m
Record.Combine({})
```

```text
[]
```

When a field name appears in more than one record, the later record's value wins.

```m
Record.Combine({[A = 1, B = 2], [B = 3, C = 4]})
```

```text
[A = 1, B = 3, C = 4]
```
