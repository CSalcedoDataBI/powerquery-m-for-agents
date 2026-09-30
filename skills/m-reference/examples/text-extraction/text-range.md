<!-- lab: desktop 2.157.879.0 -->

# Text.Range

Unlike Text.Middle, an offset past the end is an error.

```m
{Text.Range("Hello", 1, 3), Text.Range("Hello", 10)}
```

```text
{"ell", error: Expression.Error: The 'offset' argument is out of range. | Detail: 10}
```
