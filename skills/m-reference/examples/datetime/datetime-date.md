<!-- lab: desktop 2.157.879.0 -->

# DateTime.Date

Null passes through, while the time and time zone parts of a datetime value are dropped.

```m
DateTime.Date(null)
```

```text
null
```

```m
DateTime.Date(#datetime(1990, 1, 1, 23, 59, 59))
```

```text
#date(1990, 1, 1)
```

```m
DateTime.Date(#datetimezone(2200, 12, 31, 0, 0, 0, 8, 0))
```

```text
#date(2200, 12, 31)
```
