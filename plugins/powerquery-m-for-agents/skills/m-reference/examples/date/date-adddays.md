<!-- lab: desktop 2.157.879.0 -->

# Date.AddDays

Nulls propagate, negative counts move backwards across a month boundary, and the result keeps the input's type.

```m
Date.AddDays(null, 5)
```

```text
null
```

```m
Date.AddDays(#date(2011, 3, 1), -1)
```

```text
#date(2011, 2, 28)
```

```m
Date.AddDays(#datetime(2011, 5, 14, 23, 30, 0), 1)
```

```text
#datetime(2011, 5, 15, 23, 30, 0)
```
