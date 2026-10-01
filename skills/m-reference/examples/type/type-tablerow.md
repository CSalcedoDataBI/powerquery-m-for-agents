<!-- lab: desktop 2.157.879.0 -->

# Type.TableRow

These examples show that the row type keeps a column's nullability, is derived from a table's type rather than its rows, and exists even when the table has no columns.

```m
Type.TableRow(type table [A = number, B = nullable text])
```

```text
type [A = number, B = nullable text]
```

```m
Type.TableRow(Value.Type(#table(type table [A = nullable number], {{null}, {1}})))
```

```text
type [A = nullable number]
```

```m
Type.TableRow(Value.Type(#table({}, {})))
```

```text
type []
```
