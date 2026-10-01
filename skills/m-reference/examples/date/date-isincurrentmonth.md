<!-- lab: desktop 2.157.879.0 -->

# Date.IsInCurrentMonth

Nulls pass straight through, and dates far outside the current month return false however the block is run.

```m
Date.IsInCurrentMonth(null)
```

```text
null
```

```m
Date.IsInCurrentMonth(#date(1990, 1, 1))
```

```text
false
```

```m
Date.IsInCurrentMonth(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```
