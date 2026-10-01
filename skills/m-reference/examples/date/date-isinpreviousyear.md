<!-- lab: desktop 2.157.879.0 -->

# Date.IsInPreviousYear

Nulls pass through, and fixed past or future dates are not the previous year.

```m
Date.IsInPreviousYear(null)
```

```text
null
```

```m
Date.IsInPreviousYear(#date(1990, 12, 31))
```

```text
false
```

```m
Date.IsInPreviousYear(#date(2200, 1, 1))
```

```text
false
```
