<!-- lab: desktop 2.157.879.0 -->

# Date.WeekOfMonth

Nulls pass through, and the optional first day of the week changes which week a date lands in.

```m
Date.WeekOfMonth(null)
```

```text
null
```

```m
Date.WeekOfMonth(#date(2011, 3, 6))
```

```text
2
```

```m
Date.WeekOfMonth(#date(2011, 3, 6), Day.Monday)
```

```text
1
```
