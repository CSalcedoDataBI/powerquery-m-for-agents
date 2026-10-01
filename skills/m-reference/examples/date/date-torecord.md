<!-- lab: desktop 2.157.879.0 -->

# Date.ToRecord

Examples show the record of parts for a leap day, for a far-future date, and for null, which is an error rather than null.

```m
Date.ToRecord(#date(2020, 2, 29))
```

```text
[Year = 2020, Month = 2, Day = 29]
```

```m
Date.ToRecord(#date(2200, 12, 31))
```

```text
[Year = 2200, Month = 12, Day = 31]
```

```m
Date.ToRecord(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Date. | Detail: [Value = null, Type = type date]
```
