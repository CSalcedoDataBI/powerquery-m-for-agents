<!-- lab: desktop 2.157.879.0 -->

# Date.StartOfWeek

The examples show null handling, the default Sunday start, and how the optional first day of week changes it. Without the argument the result follows the query's culture: these results are for en-US, the culture the lab model sets.

```m
Date.StartOfWeek(null)
```

```text
null
```

```m
Date.StartOfWeek(#datetimezone(1990, 10, 11, 8, 10, 32, 8, 0))
```

```text
#datetimezone(1990, 10, 7, 0, 0, 0, 8, 0)
```

```m
Date.StartOfWeek(#date(2200, 10, 11), Day.Monday)
```

```text
#date(2200, 10, 6)
```
