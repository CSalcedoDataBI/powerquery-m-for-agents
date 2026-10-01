<!-- lab: desktop 2.157.879.0 -->

# Date.IsInCurrentDay

Null propagates, there are no optional arguments, and far-future date and datetimezone values never fall in the current day.

```m
Date.IsInCurrentDay(null)
```

```text
null
```

```m
Date.IsInCurrentDay(#date(2200, 1, 1))
```

```text
false
```

```m
Date.IsInCurrentDay(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```
