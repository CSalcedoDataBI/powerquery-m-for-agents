<!-- lab: desktop 2.157.879.0 -->

# Function.IsDataSource

Anonymous and library functions are not data sources, and null is rejected.

```m
Function.IsDataSource((x, optional y) => x)
```

```text
false
```

```m
Function.IsDataSource(Text.Upper)
```

```text
false
```

```m
Function.IsDataSource(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Function. | Detail: [Value = null, Type = error: Expression.Error: Function.Type is abstract and has no defined parameters.]
```
