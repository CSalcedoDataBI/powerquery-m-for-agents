<!-- lab: desktop 2.157.879.0 -->

# Date.IsInPreviousNMonths

These examples show null propagation, a zero-month window, and a far-off value that never lands in the previous months.

```m
Date.IsInPreviousNMonths(null, 3)
```

```text
null
```

```m
Date.IsInPreviousNMonths(#date(1990, 6, 15), 0)
```

```text
false
```

```m
Date.IsInPreviousNMonths(#datetime(2200, 1, 1, 12, 0, 0), 5)
```

```text
false
```
