<!-- lab: desktop 2.157.879.0 -->

# Date.DayOfWeek

The examples show how the optional first day of the week changes the numbering, that datetimezone values are accepted, and that null returns null.

```m
Date.DayOfWeek(#date(2011, 2, 21), Day.Monday)
```

```text
0
```

```m
Date.DayOfWeek(#datetimezone(2011, 2, 26, 23, 59, 59, 0, 0), Day.Sunday)
```

```text
6
```

```m
Date.DayOfWeek(null, Day.Sunday)
```

```text
null
```
