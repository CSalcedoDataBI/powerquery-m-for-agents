<!-- lab: desktop 2.157.879.0 -->

# Date.DaysInMonth

Nulls give null, and February's length depends on whether the year is a leap year.

```m
Date.DaysInMonth(null)
```

```text
null
```

A leap year's February has 29 days.

```m
Date.DaysInMonth(#date(2020, 2, 1))
```

```text
29
```

A `datetime` value is accepted too, and 2200 is a century year that is not a leap year.

```m
Date.DaysInMonth(#datetime(2200, 2, 1, 12, 30, 0))
```

```text
28
```
