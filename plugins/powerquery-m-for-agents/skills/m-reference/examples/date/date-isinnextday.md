<!-- lab: desktop 2.157.879.0 -->

# Date.IsInNextDay

Null propagates, and a value far from the current system day can never be the next day.

```m
Date.IsInNextDay(null)
```

```text
null
```

```m
Date.IsInNextDay(#date(2200, 1, 1))
```

```text
false
```

```m
Date.IsInNextDay(#datetime(1990, 12, 31, 23, 59, 59))
```

```text
false
```
