<!-- lab: desktop 2.159.883.0 -->

# DateTimeZone.ToRecord

The record holds the local date and time parts as written, plus the offset as ZoneHours and ZoneMinutes.

```m
DateTimeZone.ToRecord(#datetimezone(2024, 2, 29, 23, 59, 30.25, -3, -30))
```

```text
[Year = 2024, Month = 2, Day = 29, Hour = 23, Minute = 59, Second = 30.25, ZoneHours = -3, ZoneMinutes = -30]
```

The parts are not converted to UTC. The same instant at a different offset gives different Day and Hour fields.

```m
DateTimeZone.ToRecord(DateTimeZone.SwitchZone(#datetimezone(2024, 2, 29, 23, 59, 30.25, -3, -30), 5, 45))
```

```text
[Year = 2024, Month = 3, Day = 1, Hour = 9, Minute = 14, Second = 30.25, ZoneHours = 5, ZoneMinutes = 45]
```

A null argument.

```m
DateTimeZone.ToRecord(null)
```

```text
error: Expression.Error: We cannot convert the value null to type DateTimeZone. | Detail: [Value = null, Type = type datetimezone]
```
