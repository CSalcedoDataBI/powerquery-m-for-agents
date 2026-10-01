<!-- lab: desktop 2.157.879.0 -->

# Date.IsInPreviousNDays

A null input yields null, while dates far in the past or future never fall in a previous-day window.

```m
Date.IsInPreviousNDays(null, 2)
```

```text
null
```

A date centuries before the current day is not in the previous two days.

```m
Date.IsInPreviousNDays(#date(1990, 1, 1), 2)
```

```text
false
```

A future datetime is never in a previous window.

```m
Date.IsInPreviousNDays(#datetime(2200, 1, 1, 0, 0, 0), 1)
```

```text
false
```
