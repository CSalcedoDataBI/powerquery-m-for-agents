<!-- lab: desktop 2.157.879.0 -->

# Date.WeekOfMonth

Nulls pass through, and the optional first day of the week changes which week a date lands in. Without the argument the result follows the query's culture: these results are for en-US, the culture the lab model sets.

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
