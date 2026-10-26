<!-- lab: desktop 2.157.879.0 -->

# Date.IsInNextMonth

Nulls return null, and a date far from the current month is never in the next month.

```m
Date.IsInNextMonth(null)
```

```text
null
```

```m
Date.IsInNextMonth(#date(2200, 1, 15))
```

```text
false
```

```m
Date.IsInNextMonth(#datetimezone(1990, 12, 31, 23, 59, 59, -8, 0))
```

```text
false
```
