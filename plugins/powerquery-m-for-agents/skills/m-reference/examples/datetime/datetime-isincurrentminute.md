<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInCurrentMinute

Null input gives null, and timestamps far from now are never in the current minute.

```m
DateTime.IsInCurrentMinute(null)
```

```text
null
```

```m
DateTime.IsInCurrentMinute(#datetime(1990, 12, 31, 23, 59, 0))
```

```text
false
```

```m
DateTime.IsInCurrentMinute(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```
