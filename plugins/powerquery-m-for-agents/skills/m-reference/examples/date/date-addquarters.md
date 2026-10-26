<!-- lab: desktop 2.157.879.0 -->

# Date.AddQuarters

These examples show null propagation, end-of-month clamping, and a backward shift that keeps the time and offset.

```m
Date.AddQuarters(null, 4)
```

```text
null
```

```m
Date.AddQuarters(#date(2011, 11, 30), 1)
```

```text
#date(2012, 2, 29)
```

```m
Date.AddQuarters(#datetimezone(2200, 1, 31, 8, 15, 0, -5, 0), -1)
```

```text
#datetimezone(2199, 10, 31, 8, 15, 0, -5, 0)
```
