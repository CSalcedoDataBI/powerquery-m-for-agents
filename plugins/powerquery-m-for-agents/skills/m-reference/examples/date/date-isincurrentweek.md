<!-- lab: desktop 2.157.879.0 -->

# Date.IsInCurrentWeek

A null argument and dates fixed in 1990 and 2200 show nullable handling and the relative-to-now check.

```m
Date.IsInCurrentWeek(null)
```

```text
null
```

```m
Date.IsInCurrentWeek(#date(1990, 1, 1))
```

```text
false
```

```m
Date.IsInCurrentWeek(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```
