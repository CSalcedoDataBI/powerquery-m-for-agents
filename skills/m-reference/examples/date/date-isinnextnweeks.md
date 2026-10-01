<!-- lab: desktop 2.157.879.0 -->

# Date.IsInNextNWeeks

Nulls pass through instead of becoming false.

```m
Date.IsInNextNWeeks(null, 2)
```

```text
null
```

A date far in the future is outside the next two weeks.

```m
Date.IsInNextNWeeks(#date(2200, 1, 1), 2)
```

```text
false
```

The current week is excluded, so a zero-week window matches no date.

```m
Date.IsInNextNWeeks(#date(1990, 1, 1), 0)
```

```text
false
```
