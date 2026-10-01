<!-- lab: desktop 2.157.879.0 -->

# Date.EndOfDay

The examples show a `date` input, a `datetimezone` whose offset is preserved, and a null input.

```m
Date.EndOfDay(#date(2200, 1, 1))
```

```text
#date(2200, 1, 1)
```

```m
Date.EndOfDay(#datetimezone(1990, 12, 31, 23, 59, 59, -8, 0))
```

```text
#datetimezone(1990, 12, 31, 23, 59, 59.9999999, -8, 0)
```

```m
Date.EndOfDay(null)
```

```text
null
```
