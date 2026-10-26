<!-- lab: desktop 2.157.879.0 -->

# Date.EndOfQuarter

The examples show a null input, a date on the first day of a quarter, and a datetimezone whose offset is preserved.

```m
Date.EndOfQuarter(null)
```

```text
null
```

```m
Date.EndOfQuarter(#date(2011, 1, 1))
```

```text
#date(2011, 3, 31)
```

```m
Date.EndOfQuarter(#datetimezone(2011, 10, 10, 8, 0, 0, 9, 30))
```

```text
#datetimezone(2011, 12, 31, 23, 59, 59.9999999, 9, 30)
```
