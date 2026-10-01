<!-- lab: desktop 2.157.879.0 -->

# Date.IsInPreviousWeek

Fixed dates far from the current system week both return false, while a null argument propagates as null.

```m
Date.IsInPreviousWeek(#date(1990, 1, 1))
```

```text
false
```

```m
Date.IsInPreviousWeek(null)
```

```text
null
```

```m
Date.IsInPreviousWeek(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```
