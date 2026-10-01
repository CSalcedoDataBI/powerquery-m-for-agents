<!-- lab: desktop 2.157.879.0 -->

# Date.IsLeapYear

These examples show null handling, the century rule, and a `datetime` argument.

```m
Date.IsLeapYear(null)
```

```text
null
```

A century year divisible by 4 but not 400 is not a leap year.

```m
Date.IsLeapYear(#date(1900, 1, 1))
```

```text
false
```

A `datetime` value is evaluated the same way, and 2000 is a leap year.

```m
Date.IsLeapYear(#datetime(2000, 1, 1, 0, 0, 0))
```

```text
true
```
