<!-- lab: desktop 2.157.879.0 -->

# Type.TableColumn

These examples show how nullability is preserved and how missing or null column names behave.

```m
Type.TableColumn(type table [A = nullable text, B = number], "A")
```

```text
type nullable text
```

```m
try Type.TableColumn(type table [A = text], "B") otherwise "column not found"
```

```text
"column not found"
```

```m
try Type.TableColumn(type table [A = text], null) otherwise "column name cannot be null"
```

```text
"column name cannot be null"
```
