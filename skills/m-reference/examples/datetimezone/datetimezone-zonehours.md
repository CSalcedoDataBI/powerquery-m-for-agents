<!-- lab: desktop 2.159.883.0 -->

# DateTimeZone.ZoneHours

These examples show that only the whole-hour part of the offset is returned, that it keeps the offset's sign, and that null passes through.

```m
{
    DateTimeZone.ZoneHours(#datetimezone(2200, 1, 1, 0, 0, 0, 5, 45)),
    DateTimeZone.ZoneHours(#datetimezone(2200, 1, 1, 0, 0, 0, -3, -30)),
    DateTimeZone.ZoneHours(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
}
```

```text
{5, -3, 0}
```

The minutes are dropped. To get the full offset, combine the result with DateTimeZone.ZoneMinutes.

```m
[
    Hours = DateTimeZone.ZoneHours(#datetimezone(1990, 6, 15, 12, 0, 0, 9, 30)),
    Minutes = DateTimeZone.ZoneMinutes(#datetimezone(1990, 6, 15, 12, 0, 0, 9, 30)),
    TotalOffsetHours = Hours + Minutes / 60
]
```

```text
[Hours = 9, Minutes = 30, TotalOffsetHours = 9.5]
```

A null input gives null, not an error.

```m
DateTimeZone.ZoneHours(null)
```

```text
null
```
