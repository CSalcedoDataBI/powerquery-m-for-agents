<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInNextMinute

Nulls yield null, and fixed past or future timestamps are never in the next minute.

```m
DateTime.IsInNextMinute(null)
```

```text
null
```

```m
DateTime.IsInNextMinute(#datetime(1990, 1, 1, 0, 0, 0))
```

```text
false
```

```m
DateTime.IsInNextMinute(#datetimezone(2200, 1, 1, 0, 0, 0, 5, 0))
```

```text
false
```
