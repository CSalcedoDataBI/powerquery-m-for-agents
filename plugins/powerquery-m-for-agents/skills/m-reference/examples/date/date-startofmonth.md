<!-- lab: desktop 2.157.879.0 -->

# Date.StartOfMonth

The result keeps the input's type: a date stays a date, a datetime truncates to midnight.

```m
Date.StartOfMonth(#date(2011, 10, 10))
```

```text
#date(2011, 10, 1)
```

```m
Date.StartOfMonth(#datetime(1990, 2, 15, 8, 10, 32))
```

```text
#datetime(1990, 2, 1, 0, 0, 0)
```

```m
Date.StartOfMonth(null)
```

```text
null
```
