<!-- lab: desktop 2.157.879.0 -->

# DateTime.ToRecord

The examples show the parts record for a datetime, that null is an error rather than null, and how fractional seconds are carried.

```m
DateTime.ToRecord(#datetime(1990, 3, 15, 13, 45, 30))
```

```text
[Year = 1990, Month = 3, Day = 15, Hour = 13, Minute = 45, Second = 30]
```

```m
DateTime.ToRecord(null)
```

```text
error: Expression.Error: We cannot convert the value null to type DateTime. | Detail: [Value = null, Type = type datetime]
```

```m
DateTime.ToRecord(#datetime(2200, 12, 31, 23, 59, 59.5))
```

```text
[Year = 2200, Month = 12, Day = 31, Hour = 23, Minute = 59, Second = 59.5]
```
