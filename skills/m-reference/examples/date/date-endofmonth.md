<!-- lab: desktop 2.157.879.0 -->

# Date.EndOfMonth

Null inputs, leap-year February, and the time component of a `datetime` are the cases most easily gotten wrong.

```m
Date.EndOfMonth(null)
```

```text
null
```

```m
Date.EndOfMonth(#date(2020, 2, 10))
```

```text
#date(2020, 2, 29)
```

```m
Date.EndOfMonth(#datetime(2011, 4, 7, 9, 30, 0))
```

```text
#datetime(2011, 4, 30, 23, 59, 59.9999999)
```
