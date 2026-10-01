<!-- lab: desktop 2.157.879.0 -->

# DateTime.IsInPreviousNHours

These examples cover null input and fixed timestamps far from the current hour, so the results do not depend on when the page runs.

```m
DateTime.IsInPreviousNHours(null, 2)
```

```text
null
```

A fixed 1990 timestamp is not in the previous two hours.

```m
DateTime.IsInPreviousNHours(#datetime(1990, 1, 1, 0, 0, 0), 2)
```

```text
false
```

A datetimezone far in the future is outside the previous two hours as well.

```m
DateTime.IsInPreviousNHours(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0), 2)
```

```text
false
```
