<!-- lab: desktop 2.157.879.0 -->

# Date.StartOfQuarter

These examples show null handling and which parts of a `datetime` or `datetimezone` survive.

```m
Date.StartOfQuarter(null)
```

```text
null
```

```m
Date.StartOfQuarter(#datetime(2200, 2, 15, 13, 45, 0))
```

```text
#datetime(2200, 1, 1, 0, 0, 0)
```

```m
Date.StartOfQuarter(#datetimezone(1990, 12, 31, 23, 59, 59, 8, 0))
```

```text
#datetimezone(1990, 10, 1, 0, 0, 0, 8, 0)
```
