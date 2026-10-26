<!-- lab: desktop 2.157.879.0 -->

# Type.OpenRecord

Opening a record type adds an open marker to the outer type without changing its field types.

Opening preserves field types, including nullable ones.

```m
Type.OpenRecord(type [A = number, B = nullable text])
```

```text
type [A = number, B = nullable text, ...]
```

An already-open record type is returned unchanged.

```m
Type.OpenRecord(type [A = number, ...])
```

```text
type [A = number, ...]
```

Opening is shallow: a nested record used as a field type stays closed.

```m
Type.OpenRecord(type [Outer = [Inner = number]])
```

```text
type [Outer = [Inner = number], ...]
```
