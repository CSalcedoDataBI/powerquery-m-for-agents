<!-- lab: desktop 2.157.879.0 -->

# Date.IsInPreviousDay

Null and fixed literal values show how this current-day test behaves when the input cannot be the previous day.

```m
Date.IsInPreviousDay(null)
```

```text
null
```

```m
Date.IsInPreviousDay(#date(1990, 1, 1))
```

```text
false
```

```m
Date.IsInPreviousDay(#datetimezone(2200, 6, 15, 8, 30, 0, -5, 0))
```

```text
false
```
