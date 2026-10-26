<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInPreviousMinute

Null propagates, and fixed values far from the current minute are false even when they include a timezone.

```m
DateTime.IsInPreviousMinute(null)
```

```text
null
```

```m
DateTime.IsInPreviousMinute(#datetime(1990, 1, 1, 0, 0, 0))
```

```text
false
```

```m
DateTime.IsInPreviousMinute(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```
