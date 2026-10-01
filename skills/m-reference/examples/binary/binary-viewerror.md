<!-- lab: desktop 2.157.879.0 -->

# Binary.ViewError

A null field is allowed, an omitted field is allowed, and a null argument is rejected.

```m
Binary.ViewError([Reason = "Expression.Error", Message = "boom", Detail = null])
```

```text
[Reason = "Expression.Error", Message = "boom", Detail = null]
```

```m
Binary.ViewError([Reason = "Expression.Error", Message = "boom"])
```

```text
[Reason = "Expression.Error", Message = "boom"]
```

```m
Binary.ViewError(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Record. | Detail: [Value = null, Type = type [...]]
```
