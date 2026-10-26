<!-- lab: desktop 2.157.879.0 -->

# Date.StartOfDay

These examples show what Date.StartOfDay returns for null, a datetime, and a datetimezone value.

Passing null returns null instead of raising an error.

```m
Date.StartOfDay(null)
```

```text
null
```

A datetime keeps its date but drops the time, even from the last moment of the day.

```m
Date.StartOfDay(#datetime(2200, 3, 15, 23, 59, 59.999))
```

```text
#datetime(2200, 3, 15, 0, 0, 0)
```

A datetimezone resets the clock but preserves the original offset rather than converting to UTC.

```m
Date.StartOfDay(#datetimezone(1990, 12, 31, 18, 45, 0, -8, 0))
```

```text
#datetimezone(1990, 12, 31, 0, 0, 0, -8, 0)
```
