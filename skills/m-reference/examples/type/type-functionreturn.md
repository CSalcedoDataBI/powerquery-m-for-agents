<!-- lab: desktop 2.157.879.0 -->

# Type.FunctionReturn

These examples show the return type reported for functions with optional or nullable parameters and nullable or structured results.

```m
Type.FunctionReturn(type function (value as nullable text, optional count as number) as number)
```

```text
type number
```

```m
Type.FunctionReturn(type function (value as text) as nullable number)
```

```text
type nullable number
```

```m
Type.FunctionReturn(type function (value as number) as table [Name = text, Score = number])
```

```text
type table [Name = text, Score = number]
```
