<!-- lab: desktop 2.157.879.0 -->

# Text.Contains

Case-sensitive by default; a comparer makes it case-insensitive.

```m
{Text.Contains("Hello", "ell"), Text.Contains("Hello", "ELL"), Text.Contains("Hello", "ELL", Comparer.OrdinalIgnoreCase)}
```

```text
{true, false, true}
```
