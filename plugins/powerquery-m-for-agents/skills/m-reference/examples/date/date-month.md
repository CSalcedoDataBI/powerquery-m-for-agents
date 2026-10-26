<!-- lab: desktop 2.157.879.0 -->

# Date.Month

Null passes through, and the time part of a datetime does not affect the month.

```m
Date.Month(null)
```

```text
null
```

The last instant of a year still yields that year's month.

```m
Date.Month(#datetime(1990, 12, 31, 23, 59, 59))
```

```text
12
```

The month is taken from the value it is given, even after date arithmetic.

```m
Date.Month(Date.AddMonths(#date(2200, 1, 15), -1))
```

```text
12
```
