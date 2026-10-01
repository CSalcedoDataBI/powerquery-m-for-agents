<!-- lab: desktop 2.157.879.0 -->

# Date.Year

These examples show the year for null, datetime and datetimezone values.

A null input returns null.

```m
Date.Year(null)
```

```text
null
```

The time part of a datetime does not affect the year.

```m
Date.Year(#datetime(1990, 12, 31, 23, 59, 59))
```

```text
1990
```

A datetimezone value is accepted, and its local date determines the year.

```m
Date.Year(#datetimezone(2200, 6, 15, 12, 30, 0, -8, 0))
```

```text
2200
```
