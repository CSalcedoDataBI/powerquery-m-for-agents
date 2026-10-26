<!-- lab: desktop 2.157.879.0 -->

# Date.IsInYearToDate

A null value gives null, and dates outside the current year give false whatever the current day is.

```m
Date.IsInYearToDate(null)
```

```text
null
```

A year that is not the current year falls outside the year to date, whether it is long past or far ahead.

```m
Date.IsInYearToDate(#date(1990, 6, 15))
```

```text
false
```

The argument is typed `any`, so a `datetimezone` value is accepted as well as a `date`.

```m
Date.IsInYearToDate(#datetimezone(2200, 6, 15, 10, 30, 0, 0, 0))
```

```text
false
```
