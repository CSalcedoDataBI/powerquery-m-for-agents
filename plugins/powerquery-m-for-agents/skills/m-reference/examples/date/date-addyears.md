<!-- lab: desktop 2.157.879.0 -->

# Date.AddYears

Null input returns null.

```m
Date.AddYears(null, 4)
```

```text
null
```

A leap day clamps to the last day of February.

```m
Date.AddYears(#date(2016, 2, 29), 1)
```

```text
#date(2017, 2, 28)
```

A negative count subtracts years and preserves the time and offset.

```m
Date.AddYears(#datetimezone(1990, 5, 14, 8, 15, 22, 0, 0), -1)
```

```text
#datetimezone(1989, 5, 14, 8, 15, 22, 0, 0)
```
