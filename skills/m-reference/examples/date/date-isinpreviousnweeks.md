<!-- lab: desktop 2.157.879.0 -->

# Date.IsInPreviousNWeeks

Fixed dates far from the current week never qualify, and null passes through.

```m
Date.IsInPreviousNWeeks(#date(1990, 1, 1), 2)
```

```text
false
```

```m
Date.IsInPreviousNWeeks(#datetime(2200, 1, 1, 0, 0, 0), 1)
```

```text
false
```

```m
Date.IsInPreviousNWeeks(null, 2)
```

```text
null
```
