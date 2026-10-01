<!-- lab: desktop 2.157.879.0 -->

# Type.IsOpenRecord

These examples show that only the trailing `...` makes a record type open, while an `optional` field does not.

```m
Type.IsOpenRecord(type [A = number, ...])
```

```text
true
```

```m
Type.IsOpenRecord(type [A = number, optional B = text])
```

```text
false
```

```m
Type.IsOpenRecord(type [A = number])
```

```text
false
```
