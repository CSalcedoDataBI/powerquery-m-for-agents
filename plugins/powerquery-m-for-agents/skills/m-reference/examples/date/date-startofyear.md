<!-- lab: desktop 2.157.879.0 -->

# Date.StartOfYear

Nulls pass through, while date, datetime, and datetimezone inputs return the first instant of their year in the same type.

```m
Date.StartOfYear(null)
```

```text
null
```

A `datetime` keeps its type, dropping the time portion; this 2011 value is far enough from any run date to stay stable.

```m
Date.StartOfYear(#datetime(2011, 10, 10, 8, 10, 32))
```

```text
#datetime(2011, 1, 1, 0, 0, 0)
```

A `datetimezone` also keeps its offset, so year boundaries can shift relative to UTC.

```m
Date.StartOfYear(#datetimezone(2200, 12, 31, 23, 59, 59, 5, 30))
```

```text
#datetimezone(2200, 1, 1, 0, 0, 0, 5, 30)
```
