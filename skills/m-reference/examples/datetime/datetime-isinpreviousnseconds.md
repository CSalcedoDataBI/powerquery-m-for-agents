<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInPreviousNSeconds

Nulls pass through, while timestamps far from the current second are consistently excluded.

```m
DateTime.IsInPreviousNSeconds(null, 10)
```

```text
null
```

```m
DateTime.IsInPreviousNSeconds(#datetime(1990, 1, 1, 0, 0, 0), 60)
```

```text
false
```

```m
DateTime.IsInPreviousNSeconds(#datetimezone(2200, 12, 31, 23, 59, 59, 0, 0), 60)
```

```text
false
```
