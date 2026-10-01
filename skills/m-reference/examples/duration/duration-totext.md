<!-- lab: desktop 2.157.879.0 -->

# Duration.ToText

These examples show null propagation, a `format` argument that is now an error, and sub-day durations.

```m
Duration.ToText(null)
```

```text
null
```

```m
Duration.ToText(#duration(0, 5, 6, 7), null)
```

```text
"05:06:07"
```

```m
Duration.ToText(#duration(1, 2, 3, 4), "d.hh:mm:ss")
```

```text
error: Expression.Error: The "format" parameter of Duration.ToText has no effect and is no longer supported.
```
