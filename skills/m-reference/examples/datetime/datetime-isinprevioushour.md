<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInPreviousHour

Nulls stay null, and fixed datetime values outside the current hour return false.

```m
DateTime.IsInPreviousHour(null)
```

```text
null
```

A datetime from far in the past is never treated as the previous hour.

```m
DateTime.IsInPreviousHour(#datetime(1990, 1, 1, 0, 0, 0))
```

```text
false
```

The same false result holds for a far-future datetimezone value.

```m
DateTime.IsInPreviousHour(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```
