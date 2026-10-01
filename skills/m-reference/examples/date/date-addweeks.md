<!-- lab: desktop 2.157.879.0 -->

# Date.AddWeeks

Adding weeks propagates nulls, preserves time and zone information, and accepts negative counts.

```m
Date.AddWeeks(null, 1)
```

```text
null
```

```m
Date.AddWeeks(#datetime(1990, 12, 31, 23, 59, 59), -2)
```

```text
#datetime(1990, 12, 17, 23, 59, 59)
```

```m
Date.AddWeeks(#datetimezone(2200, 1, 1, 0, 0, 0, 8, 0), 1)
```

```text
#datetimezone(2200, 1, 8, 0, 0, 0, 8, 0)
```
