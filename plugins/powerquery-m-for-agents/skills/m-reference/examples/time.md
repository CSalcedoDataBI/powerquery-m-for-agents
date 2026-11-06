<!-- lab: desktop 2.159.883.0 -->

# Executed examples: time

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Time.From

Text, numbers and datetimes convert to a time; null stays null.

```m
{Time.From(null), Time.From(0.75), Time.From(#datetime(2200, 1, 1, 13, 45, 0)), Time.From("10:12:31pm")}
```

```text
{null, #time(18, 0, 0), #time(13, 45, 0), #time(22, 12, 31)}
```

The culture argument changes how text is parsed.

```m
{Time.From("15:30", "de-DE"), Time.From("3:30 PM", "en-US")}
```

```text
{#time(15, 30, 0), #time(15, 30, 0)}
```

A number is read as a fraction of a day, so whole days may not be allowed.

```m
try Time.From(1.5)
```

```text
[HasError = true, Error = [Reason = "DataFormat.Error", Message = "We couldn't convert to Time.", Detail = 1.5, #"Message.Format" = "We couldn't convert to Time.", #"Message.Parameters" = null, ErrorCode = "10333"]]
```

## Time.FromText

These examples show that null text returns null, that a custom format can ignore a date part, and that the culture option reads 12-hour times.

```m
{Time.FromText(null), Time.FromText("10:12:31", [Culture = "en-US"])}
```

```text
{null, #time(10, 12, 31)}
```

A `Format` string that includes a date component is rejected, even when the text also carries a time: the engine returns a `Parameter.Error` rather than keeping the time part.

```m
Time.FromText("30 Dec 2010 02:04:50.369730", [Format = "dd MMM yyyy HH:mm:ss.ffffff", Culture = "en-US"])
```

```text
error: Parameter.Error: We couldn't use the specified value as a time format because it includes a date component. | Detail: [Format = "dd MMM yyyy HH:mm:ss.ffffff"]
```

The 12-hour pattern `hh` together with `tt` reads the AM/PM marker. The pattern `HH` reads a 24-hour value.

```m
{Time.FromText("02:30 PM", [Format = "hh:mm tt", Culture = "en-US"]), Time.FromText("14:30", [Format = "HH:mm", Culture = "en-US"])}
```

```text
{#time(14, 30, 0), #time(14, 30, 0)}
```

## Time.Hour

The examples show which hour comes back for time zones, nulls and edge times.

On a datetimezone, the hour stays in the value's own offset and is not converted to UTC.

```m
Time.Hour(#datetimezone(1990, 6, 1, 23, 30, 0, -5, 0))
```

```text
23
```

A null input returns null, and the hour never rounds up from minutes or seconds.

```m
{Time.Hour(null), Time.Hour(#time(9, 59, 59.9)), Time.Hour(#datetime(1990, 1, 1, 0, 0, 0))}
```

```text
{null, 9, 0}
```

The time literal accepts 24:00:00.

```m
Time.Hour(#time(24, 0, 0))
```

```text
0
```

## Time.Minute

The minute is read as written: seconds never round it up, a zone offset never shifts it, and null passes through.

```m
Time.Minute(#time(9, 59, 59.999))
```

```text
59
```

The minute comes from the local time, not from the UTC equivalent.

```m
Time.Minute(#datetimezone(2011, 12, 31, 9, 15, 36, 5, 30))
```

```text
15
```

```m
Time.Minute(null)
```

```text
null
```

## Time.Second

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

## Time.ToRecord

The examples show fractional seconds, the 24:00 edge case, and a null input.

```m
Time.ToRecord(#time(14, 5, 30.25))
```

```text
[Hour = 14, Minute = 5, Second = 30.25]
```

```m
Time.ToRecord(#time(24, 0, 0))
```

```text
[Hour = 0, Minute = 0, Second = 0]
```

```m
Time.ToRecord(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Time. | Detail: [Value = null, Type = type time]
```

## Time.ToText

Format strings, culture, and null input.

```m
Time.ToText(#time(14, 5, 9), [Format = "hh:mm tt", Culture = "en-US"])
```

```text
"02:05 PM"
```

```m
Time.ToText(#time(14, 5, 9), [Format = "HH:mm:ss", Culture = "de-DE"])
```

```text
"14:05:09"
```

```m
Time.ToText(null)
```

```text
null
```
