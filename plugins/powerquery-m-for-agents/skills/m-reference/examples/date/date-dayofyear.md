<!-- lab: desktop 2.157.879.0 -->

# Date.DayOfYear

The examples show how a null input is handled, how leap years affect the count, and how the time part of a value is ignored.

```m
Date.DayOfYear(null)
```

```text
null
```

A leap day sits at the same position as the March 1 of a common year.

```m
Date.DayOfYear(#date(2020, 2, 29))
```

```text
60
```

A `datetime` is accepted, and its time portion does not change the result.

```m
Date.DayOfYear(#datetime(2019, 3, 1, 23, 59, 59))
```

```text
60
```
