<!-- lab: desktop 2.157.879.0 -->

# Duration.Minutes

Null in gives null out.

```m
Duration.Minutes(null)
```

```text
null
```

Minutes above 59 carry into the hours, so this returns 15 rather than 75.

```m
Duration.Minutes(#duration(0, 2, 75, 0))
```

```text
15
```

A whole number of hours has no leftover minutes, so this is 0 even though the duration holds 300 minutes.

```m
Duration.Minutes(#duration(0, 5, 0, 0))
```

```text
0
```
