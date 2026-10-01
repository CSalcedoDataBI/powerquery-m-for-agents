<!-- lab: desktop 2.157.879.0 -->

# Type.ClosedRecord

Closing an open record type drops the `...` marker while keeping each field's type, its `optional` marker and its `nullable` facet.

```m
Type.ClosedRecord(type [A = number, optional B = text, ...])
```

```text
type [A = number, optional B = text]
```

A nullability facet on a field type survives closing.

```m
Type.ClosedRecord(type [A = nullable number, ...])
```

```text
type [A = nullable number]
```

An already-closed record type is returned unchanged, so closing twice is the same as closing once.

```m
Type.ClosedRecord(Type.ClosedRecord(type [A = number, ...]))
```

```text
type [A = number]
```
