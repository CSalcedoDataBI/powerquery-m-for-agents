<!-- lab: desktop 2.159.883.0 -->

# Executed examples: datetimezone

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## DateTimeZone.From

Null passes through as null, and text keeps the offset it is written with.

```m
[
    FromNull = DateTimeZone.From(null),
    FromText = DateTimeZone.From("2020-01-15T10:30:00+05:00"),
    FromValue = DateTimeZone.From(#datetimezone(2200, 1, 1, 0, 0, 0, -8, 0))
]
```

```text
[FromNull = null, FromText = #datetimezone(2020, 1, 15, 10, 30, 0, 5, 0), FromValue = #datetimezone(2200, 1, 1, 0, 0, 0, -8, 0)]
```

The optional culture decides whether "03/04" is read as March 4 or April 3.

```m
[
    US = DateTimeZone.From("03/04/2020 10:00 +01:00", "en-US"),
    GB = DateTimeZone.From("03/04/2020 10:00 +01:00", "en-GB")
]
```

```text
[US = #datetimezone(2020, 3, 4, 10, 0, 0, 1, 0), GB = #datetimezone(2020, 4, 3, 10, 0, 0, 1, 0)]
```

## DateTimeZone.FromText

A null input returns null, a trailing "Z" means a +00:00 offset, and the optional options argument can set a custom format and culture.

```m
{DateTimeZone.FromText(null), DateTimeZone.FromText("2010-12-31T01:30:00-08:00"), DateTimeZone.FromText("2010-12-31T01:30:00Z")}
```

```text
{null, #datetimezone(2010, 12, 31, 1, 30, 0, -8, 0), #datetimezone(2010, 12, 31, 1, 30, 0, 0, 0)}
```

With a custom format, month names are read in the given culture.

```m
DateTimeZone.FromText("30 Dez 2010 02:04:50.369730 +02:00", [Format = "dd MMM yyyy HH:mm:ss.ffffff zzz", Culture = "de-DE"])
```

```text
#datetimezone(2010, 12, 30, 2, 4, 50.36973, 2, 0)
```

A culture alone decides the day and month order of an ambiguous date.

```m
{DateTimeZone.FromText("03/04/2010 10:00:00 +01:00", [Culture = "en-GB"]), DateTimeZone.FromText("03/04/2010 10:00:00 +01:00", [Culture = "en-US"])}
```

```text
{#datetimezone(2010, 4, 3, 10, 0, 0, 1, 0), #datetimezone(2010, 3, 4, 10, 0, 0, 1, 0)}
```

## DateTimeZone.RemoveZone

The offset is dropped without being applied, so the clock time stays as written.

```m
DateTimeZone.RemoveZone(#datetimezone(2024, 3, 10, 14, 30, 0, 5, 30))
```

```text
#datetime(2024, 3, 10, 14, 30, 0)
```

To get the UTC clock time, convert first and then remove the zone.

```m
[
    Dropped = DateTimeZone.RemoveZone(#datetimezone(2024, 3, 10, 14, 30, 0, 5, 30)),
    UtcFirst = DateTimeZone.RemoveZone(DateTimeZone.ToUtc(#datetimezone(2024, 3, 10, 14, 30, 0, 5, 30))),
    NegativeOffset = DateTimeZone.RemoveZone(DateTimeZone.ToUtc(#datetimezone(2024, 12, 31, 22, 0, 0, -5, 0)))
]
```

```text
[Dropped = #datetime(2024, 3, 10, 14, 30, 0), UtcFirst = #datetime(2024, 3, 10, 9, 0, 0), NegativeOffset = #datetime(2025, 1, 1, 3, 0, 0)]
```

A null input passes through as null.

```m
DateTimeZone.RemoveZone(null)
```

```text
null
```

## DateTimeZone.SwitchZone

The instant stays the same, so the clock time and even the date shift, and a null input returns null.

```m
DateTimeZone.SwitchZone(#datetimezone(2010, 12, 31, 23, 0, 0, 0, 0), 5, 30)
```

```text
#datetimezone(2011, 1, 1, 4, 30, 0, 5, 30)
```

For a negative offset with minutes, give the minutes the same sign as the hours.

```m
DateTimeZone.SwitchZone(#datetimezone(2010, 12, 31, 1, 0, 0, 7, 0), -3, -30)
```

```text
#datetimezone(2010, 12, 30, 14, 30, 0, -3, -30)
```

```m
DateTimeZone.SwitchZone(null, 3)
```

```text
null
```

## DateTimeZone.ToRecord

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

## DateTimeZone.ToText

These examples show null input, the options record, and the older text-format argument with a negative offset.

```m
{DateTimeZone.ToText(null), DateTimeZone.ToText(#datetimezone(2010, 12, 31, 1, 30, 25, 2, 0))}
```

```text
{null, "12/31/2010 1:30:25 AM +02:00"}
```

An options record sets the format and culture together, and `zzz` writes the offset.

```m
DateTimeZone.ToText(#datetimezone(2010, 12, 31, 1, 30, 25, 2, 0), [Format = "yyyy-MM-ddTHH:mm:sszzz", Culture = "en-US"])
```

```text
"2010-12-31T01:30:25+02:00"
```

A text format can also be passed directly as the second argument, with the culture as the third argument.

```m
DateTimeZone.ToText(#datetimezone(2010, 12, 31, 1, 30, 25, -5, -30), "dd MMMM yyyy HH:mm zzz", "fr-FR")
```

```text
"31 décembre 2010 01:30 -05:30"
```

## DateTimeZone.ToUtc

The examples show that the clock time shifts by the offset, which can cross a date or year boundary, and that null passes through unchanged.

```m
DateTimeZone.ToUtc(#datetimezone(2010, 12, 31, 22, 30, 0, -5, -30))
```

```text
#datetimezone(2011, 1, 1, 4, 0, 0, 0, 0)
```

Different offsets for the same instant give the same UTC value.

```m
{
    DateTimeZone.ToUtc(#datetimezone(2024, 3, 1, 5, 30, 0, 5, 30)),
    DateTimeZone.ToUtc(#datetimezone(2024, 2, 29, 16, 0, 0, -8, 0)),
    DateTimeZone.ToUtc(#datetimezone(2024, 3, 1, 0, 0, 0, 0, 0))
}
```

```text
{#datetimezone(2024, 3, 1, 0, 0, 0, 0, 0), #datetimezone(2024, 3, 1, 0, 0, 0, 0, 0), #datetimezone(2024, 3, 1, 0, 0, 0, 0, 0)}
```

A null input returns null instead of raising an error.

```m
DateTimeZone.ToUtc(null)
```

```text
null
```

## DateTimeZone.ZoneHours

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

## DateTimeZone.ZoneMinutes

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
