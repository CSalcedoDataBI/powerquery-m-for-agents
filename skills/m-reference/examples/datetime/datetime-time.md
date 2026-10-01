<!-- lab: desktop 2.157.879.0 -->

# DateTime.Time

The examples show the time part of a datetime, a date refused because it has no time, and null passing through.

```m
DateTime.Time(#datetime(2200, 6, 15, 4, 5, 6))
```

```text
#time(4, 5, 6)
```

```m
DateTime.Time(#date(1990, 1, 1))
```

```text
error: Expression.Error: The DateTime.Time function expects an input of type DateTime or DateTimeZone. | Detail: #date(1990, 1, 1)
```

```m
DateTime.Time(null)
```

```text
null
```
