<!-- lab: desktop 2.157.879.0 -->

# Time.EndOfHour

These examples show how nulls, time-only values, and a non-UTC zone offset are handled.

```m
Time.EndOfHour(null)
```

```text
null
```

```m
Time.EndOfHour(#time(5, 0, 0))
```

```text
#time(5, 59, 59.9999999)
```

```m
Time.EndOfHour(#datetimezone(2200, 1, 1, 0, 0, 0, 5, 30))
```

```text
#datetimezone(2200, 1, 1, 0, 59, 59.9999999, 5, 30)
```
