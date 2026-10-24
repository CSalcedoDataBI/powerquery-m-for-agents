<!-- lab: desktop 2.159.883.0 -->

# Time.Second

These examples show that Time.Second keeps fractional seconds, accepts time, datetime and datetimezone values, and returns null for null.

```m
[
    FromTime = Time.Second(#time(9, 15, 36.5)),
    FromDateTime = Time.Second(#datetime(2011, 12, 31, 9, 15, 36.5)),
    FromText = Time.Second(Time.From("23:59:59.9999999"))
]
```

```text
[FromTime = 36.5, FromDateTime = 36.5, FromText = 59.9999999]
```

```m
[
    FromDateTimeZone = Time.Second(#datetimezone(2011, 12, 31, 9, 15, 36, -8, 0)),
    FromNull = Time.Second(null),
    Midnight = Time.Second(#time(24, 0, 0))
]
```

```text
[FromDateTimeZone = 36, FromNull = null, Midnight = 0]
```

```m
try Time.Second(#date(2011, 12, 31))
```

```text
[HasError = true, Error = [Reason = "Expression.Error", Message = "The Time value must contain the Time component.", Detail = #date(2011, 12, 31), #"Message.Format" = "The Time value must contain the #{0} component.", #"Message.Parameters" = {"Time"}, ErrorCode = "10024"]]
```
