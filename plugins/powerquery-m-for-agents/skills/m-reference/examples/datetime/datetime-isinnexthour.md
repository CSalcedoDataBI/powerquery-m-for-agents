<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInNextHour

Fixed past and future dates, plus null, show how the function treats values outside the hour after the current system time.

```m
DateTime.IsInNextHour(#datetime(2200, 1, 1, 0, 0, 0))
```

```text
false
```

```m
DateTime.IsInNextHour(#datetimezone(1990, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

```m
DateTime.IsInNextHour(null)
```

```text
null
```
