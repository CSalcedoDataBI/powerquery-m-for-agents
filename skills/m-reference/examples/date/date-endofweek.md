<!-- lab: desktop 2.157.879.0 -->

# Date.EndOfWeek

These examples show null input, the default first day of the week, and an explicit first day with a timezone value.

A null date returns null.

```m
Date.EndOfWeek(null)
```

```text
null
```

With no first-day argument, the week uses the default Sunday.

```m
Date.EndOfWeek(#date(1990, 1, 1))
```

```text
#date(1990, 1, 6)
```

An explicit `Day.Monday` changes the week boundary, and a timezone value keeps its offset.

```m
Date.EndOfWeek(#datetimezone(2200, 1, 1, 5, 0, 0, -7, 0), Day.Monday)
```

```text
#datetimezone(2200, 1, 5, 23, 59, 59.9999999, -7, 0)
```
