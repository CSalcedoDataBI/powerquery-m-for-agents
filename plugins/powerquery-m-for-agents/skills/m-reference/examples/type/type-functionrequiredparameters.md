<!-- lab: desktop 2.157.879.0 -->

# Type.FunctionRequiredParameters

These examples show that only parameters not declared `optional` are counted.

```m
Type.FunctionRequiredParameters(type function (x as number, y as text) as any)
```

```text
2
```

An `optional` parameter does not raise the required count.

```m
Type.FunctionRequiredParameters(type function (x as number, optional y as text) as any)
```

```text
1
```

A function whose parameters are all optional requires none.

```m
Type.FunctionRequiredParameters(type function (optional x as number, optional y as text) as any)
```

```text
0
```
