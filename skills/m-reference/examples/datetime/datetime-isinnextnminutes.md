<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInNextNMinutes

Nulls pass through, and fixed past or future datetimes fall outside the next-minute window regardless of when the block runs.

```m
DateTime.IsInNextNMinutes(null, 5)
```

```text
null
```

```m
DateTime.IsInNextNMinutes(#datetime(1990, 12, 31, 23, 59, 0), 5)
```

```text
false
```

```m
DateTime.IsInNextNMinutes(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0), 60)
```

```text
false
```
