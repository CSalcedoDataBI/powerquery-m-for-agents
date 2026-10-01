<!-- lab: desktop 2.157.879.0 -->

# Logical.ToText

These examples show the lowercase text produced for a logical value, that null passes through as null, and that a non-logical value raises an error.

```m
Logical.ToText(true)
```

```text
"true"
```

```m
Logical.ToText(null)
```

```text
null
```

```m
Logical.ToText(1)
```

```text
error: Expression.Error: We cannot convert the value 1 to type Logical. | Detail: [Value = 1, Type = type nullable logical]
```
