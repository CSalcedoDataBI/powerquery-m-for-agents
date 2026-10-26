<!-- lab: desktop 2.157.879.0 -->

# Logical.FromText

These examples show case-insensitive conversion, null handling, and invalid input.

```m
Logical.FromText("TRUE")
```

```text
true
```

```m
Logical.FromText(null)
```

```text
null
```

```m
Logical.FromText("a")
```

```text
error: Expression.Error: We couldn't convert to Logical. | Detail: "a"
```
