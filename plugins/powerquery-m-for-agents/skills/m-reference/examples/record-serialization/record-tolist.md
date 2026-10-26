<!-- lab: desktop 2.157.879.0 -->

# Record.ToList

Collecting a record's field values keeps nulls, follows declaration order, and handles the empty record.

Null field values are kept as items, not dropped.

```m
Record.ToList([A = null, B = 2, C = null])
```

```text
{null, 2, null}
```

The values come out in the order the fields are declared, not in name order.

```m
Record.ToList([C = 3, A = 1])
```

```text
{3, 1}
```

An empty record produces an empty list.

```m
Record.ToList([])
```

```text
{}
```
