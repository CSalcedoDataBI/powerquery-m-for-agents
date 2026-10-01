<!-- lab: desktop 2.157.879.0 -->

# Date.Day

The examples show the day component for null, a `datetime`, and a `datetimezone` value.

```m
Date.Day(null)
```

```text
null
```

A `datetime` reports its calendar day even one second before midnight.

```m
Date.Day(#datetime(1990, 1, 31, 23, 59, 59))
```

```text
31
```

A `datetimezone` reports the day in its stored local time, not the UTC instant.

```m
Date.Day(#datetimezone(2200, 12, 31, 23, 30, 0, -8, 0))
```

```text
31
```
