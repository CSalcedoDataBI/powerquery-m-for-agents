<!-- lab: desktop 2.157.879.0 -->

# Executed examples: datetime

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## DateTime.AddZone

These examples show how a null datetime, the optional minutes argument, and a negative offset behave.

Attaching a zone to a null datetime returns null.

```m
DateTime.AddZone(null, 7, 30)
```

```text
null
```

When the optional minutes argument is omitted, it defaults to zero.

```m
DateTime.AddZone(#datetime(2010, 12, 31, 11, 56, 2), -5)
```

```text
#datetimezone(2010, 12, 31, 11, 56, 2, -5, 0)
```

The offset never shifts the clock digits, even at the end of a day.

```m
DateTime.AddZone(#datetime(2200, 6, 15, 23, 59, 59), -3, -30)
```

```text
#datetimezone(2200, 6, 15, 23, 59, 59, -3, -30)
```

## DateTime.Date

Null passes through, while the time and time zone parts of a datetime value are dropped.

```m
DateTime.Date(null)
```

```text
null
```

```m
DateTime.Date(#datetime(1990, 1, 1, 23, 59, 59))
```

```text
#date(1990, 1, 1)
```

```m
DateTime.Date(#datetimezone(2200, 12, 31, 0, 0, 0, 8, 0))
```

```text
#date(2200, 12, 31)
```

## DateTime.From

These examples show the null result, the optional culture argument, and the date chosen when converting a time.

```m
DateTime.From(null)
```

```text
null
```

```m
DateTime.From("12/31/1990 11:59:59 PM", "en-US")
```

```text
#datetime(1990, 12, 31, 23, 59, 59)
```

```m
DateTime.From(#time(6, 45, 12))
```

```text
#datetime(1899, 12, 30, 6, 45, 12)
```

## DateTime.FromText

The examples show null input, the legacy text form of the options argument, and culture-sensitive parsing with an explicit format.

```m
DateTime.FromText(null)
```

```text
null
```

```m
DateTime.FromText("01/02/2010 03:04:05", "en-GB")
```

```text
#datetime(2010, 2, 1, 3, 4, 5)
```

```m
DateTime.FromText("30 Dez 2010 02:04:50.369730", [Format = "dd MMM yyyy HH:mm:ss.ffffff", Culture = "de-DE"])
```

```text
#datetime(2010, 12, 30, 2, 4, 50.36973)
```

## DateTime.IsInCurrentHour

Distant instants are never in the current hour, a time-zone value behaves the same way, and null stays null.

```m
DateTime.IsInCurrentHour(#datetime(1990, 1, 1, 0, 0, 0))
```

```text
false
```

A `datetimezone` value from the far future is likewise outside the current hour.

```m
DateTime.IsInCurrentHour(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

A null input is not treated as false.

```m
DateTime.IsInCurrentHour(null)
```

```text
null
```

## DateTime.IsInCurrentMinute

Null input gives null, and timestamps far from now are never in the current minute.

```m
DateTime.IsInCurrentMinute(null)
```

```text
null
```

```m
DateTime.IsInCurrentMinute(#datetime(1990, 12, 31, 23, 59, 0))
```

```text
false
```

```m
DateTime.IsInCurrentMinute(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

## DateTime.IsInCurrentSecond

These examples show how the check treats null and fixed timestamps far from the present.

```m
DateTime.IsInCurrentSecond(null)
```

```text
null
```

```m
DateTime.IsInCurrentSecond(#datetime(1990, 1, 1, 0, 0, 0))
```

```text
false
```

```m
DateTime.IsInCurrentSecond(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

## DateTime.IsInNextHour

Fixed past and future dates, plus null, show how the function treats values outside the hour after the current system time.

```m
DateTime.IsInNextHour(#datetime(2200, 1, 1, 0, 0, 0))
```

```text
false
```

```m
DateTime.IsInNextHour(#datetimezone(1990, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

```m
DateTime.IsInNextHour(null)
```

```text
null
```

## DateTime.IsInNextMinute

Nulls yield null, and fixed past or future timestamps are never in the next minute.

```m
DateTime.IsInNextMinute(null)
```

```text
null
```

```m
DateTime.IsInNextMinute(#datetime(1990, 1, 1, 0, 0, 0))
```

```text
false
```

```m
DateTime.IsInNextMinute(#datetimezone(2200, 1, 1, 0, 0, 0, 5, 0))
```

```text
false
```

## DateTime.IsInNextNHours

A null value gives a null result.

```m
DateTime.IsInNextNHours(null, 3)
```

```text
null
```

A datetime far in the past is never in the next few hours.

```m
DateTime.IsInNextNHours(#datetime(1990, 1, 1, 0, 0, 0), 3)
```

```text
false
```

A far-future datetime qualifies only when the hour window reaches it.

```m
DateTime.IsInNextNHours(#datetime(2200, 1, 1, 0, 0, 0), 2000000)
```

```text
true
```

## DateTime.IsInNextNMinutes

Nulls pass through, and fixed past or future datetimes fall outside the next-minute window regardless of when the block runs.

```m
DateTime.IsInNextNMinutes(null, 5)
```

```text
null
```

```m
DateTime.IsInNextNMinutes(#datetime(1990, 12, 31, 23, 59, 0), 5)
```

```text
false
```

```m
DateTime.IsInNextNMinutes(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0), 60)
```

```text
false
```

## DateTime.IsInNextNSeconds

Null propagates, a fixed far-past value stays outside the window, and a far-future value can fall inside a very long window.

```m
DateTime.IsInNextNSeconds(null, 10)
```

```text
null
```

```m
DateTime.IsInNextNSeconds(#datetime(1990, 1, 1, 0, 0, 0), 60)
```

```text
false
```

```m
DateTime.IsInNextNSeconds(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0), 10000000000)
```

```text
true
```

## DateTime.IsInNextSecond

Only the one-second window after the current instant counts, while null and far-off values fall outside it.

A null input yields null rather than false.

```m
DateTime.IsInNextSecond(null)
```

```text
null
```

A datetime far in the past is never in the next second, regardless of the current system time.

```m
DateTime.IsInNextSecond(#datetime(1990, 12, 31, 23, 59, 59))
```

```text
false
```

A datetimezone in the far future is likewise false, since neither the date nor its offset can pull it into the next second.

```m
DateTime.IsInNextSecond(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

## DateTime.IsInPreviousHour

Nulls stay null, and fixed datetime values outside the current hour return false.

```m
DateTime.IsInPreviousHour(null)
```

```text
null
```

A datetime from far in the past is never treated as the previous hour.

```m
DateTime.IsInPreviousHour(#datetime(1990, 1, 1, 0, 0, 0))
```

```text
false
```

The same false result holds for a far-future datetimezone value.

```m
DateTime.IsInPreviousHour(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

## DateTime.IsInPreviousMinute

Null propagates, and fixed values far from the current minute are false even when they include a timezone.

```m
DateTime.IsInPreviousMinute(null)
```

```text
null
```

```m
DateTime.IsInPreviousMinute(#datetime(1990, 1, 1, 0, 0, 0))
```

```text
false
```

```m
DateTime.IsInPreviousMinute(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

## DateTime.IsInPreviousNHours

These examples cover null input and fixed timestamps far from the current hour, so the results do not depend on when the page runs.

```m
DateTime.IsInPreviousNHours(null, 2)
```

```text
null
```

A fixed 1990 timestamp is not in the previous two hours.

```m
DateTime.IsInPreviousNHours(#datetime(1990, 1, 1, 0, 0, 0), 2)
```

```text
false
```

A datetimezone far in the future is outside the previous two hours as well.

```m
DateTime.IsInPreviousNHours(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0), 2)
```

```text
false
```

## DateTime.IsInPreviousNMinutes

The window is anchored to the current clock, so timestamps far in the past or future fall outside it even for a large `minutes` value.

```m
DateTime.IsInPreviousNMinutes(#datetime(1990, 1, 1, 0, 0, 0), 5)
```

```text
false
```

A `datetimezone` value is accepted in place of a `datetime`.

```m
DateTime.IsInPreviousNMinutes(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0), 5)
```

```text
false
```

A null `dateTime` returns null rather than false.

```m
DateTime.IsInPreviousNMinutes(null, 5)
```

```text
null
```

## DateTime.IsInPreviousNSeconds

Nulls pass through, while timestamps far from the current second are consistently excluded.

```m
DateTime.IsInPreviousNSeconds(null, 10)
```

```text
null
```

```m
DateTime.IsInPreviousNSeconds(#datetime(1990, 1, 1, 0, 0, 0), 60)
```

```text
false
```

```m
DateTime.IsInPreviousNSeconds(#datetimezone(2200, 12, 31, 23, 59, 59, 0, 0), 60)
```

```text
false
```

## DateTime.IsInPreviousSecond

These examples show a value far from the current second, a null argument, and a `datetimezone` value.

```m
DateTime.IsInPreviousSecond(#datetime(1990, 1, 1, 0, 0, 0))
```

```text
false
```

```m
DateTime.IsInPreviousSecond(null)
```

```text
null
```

```m
DateTime.IsInPreviousSecond(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

## DateTime.Time

The examples show the time part of a datetime, a date refused because it has no time, and null passing through.

```m
DateTime.Time(#datetime(2200, 6, 15, 4, 5, 6))
```

```text
#time(4, 5, 6)
```

```m
DateTime.Time(#date(1990, 1, 1))
```

```text
error: Expression.Error: The DateTime.Time function expects an input of type DateTime or DateTimeZone. | Detail: #date(1990, 1, 1)
```

```m
DateTime.Time(null)
```

```text
null
```

## DateTime.ToRecord

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

## DateTime.ToText

These examples show how a null input, the legacy text `options` form, and a record that omits `Format` behave.

```m
DateTime.ToText(null)
```

```text
null
```

```m
DateTime.ToText(#datetime(2010, 12, 30, 2, 4, 50.36973), "dd MMM yyyy", "de-DE")
```

```text
"30 Dez 2010"
```

```m
DateTime.ToText(#datetime(2010, 12, 31, 13, 30, 25), [Format = null, Culture = "en-US"])
```

```text
"12/31/2010 1:30:25 PM"
```
