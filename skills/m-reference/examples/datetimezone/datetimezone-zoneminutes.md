<!-- lab: desktop 2.159.883.0 -->

# DateTimeZone.ZoneMinutes

These examples show that the minute part of the offset takes the offset's sign, and that null passes through.

```m
{
    DateTimeZone.ZoneMinutes(#datetimezone(2020, 1, 1, 0, 0, 0, 5, 45)),
    DateTimeZone.ZoneMinutes(#datetimezone(2020, 1, 1, 0, 0, 0, -3, -30)),
    DateTimeZone.ZoneMinutes(#datetimezone(2020, 1, 1, 0, 0, 0, 2, 0))
}
```

```text
{45, -30, 0}
```

An offset under one hour has zero hours, so only the minutes carry the sign.

```m
[
    Hours = DateTimeZone.ZoneHours(DateTimeZone.FromText("2020-01-01T00:00:00-00:30")),
    Minutes = DateTimeZone.ZoneMinutes(DateTimeZone.FromText("2020-01-01T00:00:00-00:30"))
]
```

```text
[Hours = 0, Minutes = -30]
```

A null input returns null instead of an error.

```m
DateTimeZone.ZoneMinutes(null)
```

```text
null
```
