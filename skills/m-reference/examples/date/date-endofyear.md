<!-- lab: desktop 2.157.879.0 -->

# Date.EndOfYear

A `date` argument keeps the `date` type.

```m
Date.EndOfYear(#date(1990, 3, 15))
```

```text
#date(1990, 12, 31)
```

Time zone information is preserved.

```m
Date.EndOfYear(#datetimezone(2200, 7, 4, 13, 45, 30, 5, 30))
```

```text
#datetimezone(2200, 12, 31, 23, 59, 59.9999999, 5, 30)
```

A `null` argument returns `null`.

```m
Date.EndOfYear(null)
```

```text
null
```
