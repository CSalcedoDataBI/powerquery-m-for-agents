<!-- lab: desktop 2.157.879.0 -->

# Type.FunctionParameters

These examples show how a function's parameters come back as a record of `type` values, including optional and `any` parameters.

```m
Type.FunctionParameters(type function (x as any, y as text) as any)
```

```text
[x = type any, y = type text]
```

An optional parameter is listed like a required one, with its type made nullable.

```m
Type.FunctionParameters(type function (start as number, optional end as number) as any)
```

```text
[start = type number, end = type nullable number]
```

A function that takes no parameters yields an empty record.

```m
Type.FunctionParameters(type function () as any)
```

```text
[]
```
