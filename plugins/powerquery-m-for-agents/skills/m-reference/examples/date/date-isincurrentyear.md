<!-- lab: desktop 2.157.879.0 -->

# Date.IsInCurrentYear

These examples test how a null value and dates far outside the current year behave.

```m
Date.IsInCurrentYear(null)
```

```text
null
```

```m
Date.IsInCurrentYear(#date(1990, 3, 15))
```

```text
false
```

```m
Date.IsInCurrentYear(#datetime(2200, 12, 31, 23, 59, 59))
```

```text
false
```
