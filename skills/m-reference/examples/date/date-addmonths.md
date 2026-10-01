<!-- lab: desktop 2.157.879.0 -->

# Date.AddMonths

These examples show month-end clamping, negative month counts, and null input.

```m
Date.AddMonths(#date(1990, 1, 31), 1)
```

```text
#date(1990, 2, 28)
```

```m
Date.AddMonths(#datetimezone(2200, 3, 31, 8, 15, 22, 0, 0), -1)
```

```text
#datetimezone(2200, 2, 28, 8, 15, 22, 0, 0)
```

```m
Date.AddMonths(null, 5)
```

```text
null
```
