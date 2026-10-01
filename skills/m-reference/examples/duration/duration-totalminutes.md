<!-- lab: desktop 2.157.879.0 -->

# Duration.TotalMinutes

Nulls stay null, and total minutes include hours and fractions of a minute.

```m
Duration.TotalMinutes(null)
```

```text
null
```

```m
Duration.TotalMinutes(#duration(0, 1, 30, 0))
```

```text
90
```

```m
Duration.TotalMinutes(#duration(0, 0, 0, 30))
```

```text
0.5
```
