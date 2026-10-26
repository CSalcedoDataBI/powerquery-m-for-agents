<!-- lab: desktop 2.157.879.0 -->

# Executed examples: duration

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Duration.Days

The examples show the days portion of a duration, which is not the same as the total number of days.

```m
Duration.Days(#duration(1, 23, 0, 0))
```

```text
1
```

A duration shorter than one whole day has zero days.

```m
Duration.Days(#duration(0, 5, 30, 0))
```

```text
0
```

A null duration gives a null result.

```m
Duration.Days(null)
```

```text
null
```

## Duration.From

These examples show how a number, a text value, and a null each become a duration.

```m
Duration.From(2.525)
```

```text
#duration(2, 12, 36, 0)
```

Text uses the elapsed-time form `d.hh:mm:ss`, not a plain number.

```m
Duration.From("2.05:55:20.34567")
```

```text
#duration(2, 5, 55, 20.34567)
```

A null passes through instead of raising an error.

```m
Duration.From(null)
```

```text
null
```

## Duration.FromText

Null input returns null, seconds are optional, and a leading day component counts as days.

```m
Duration.FromText(null)
```

```text
null
```

```m
Duration.FromText("01:02")
```

```text
#duration(0, 1, 2, 0)
```

```m
Duration.FromText("1.01:02:03.5")
```

```text
#duration(1, 1, 2, 3.5)
```

## Duration.Hours

These examples show the hour component of a duration, including null input and an hour value that carries into days.

A null duration stays null.

```m
Duration.Hours(null)
```

```text
null
```

Only the hours field is returned, not the hours contained in the days.

```m
Duration.Hours(#duration(5, 4, 3, 2))
```

```text
4
```

Hours beyond a full day are carried into the days, so the hours field wraps.

```m
Duration.Hours(#duration(0, 25, 0, 0))
```

```text
1
```

## Duration.Minutes

Null in gives null out.

```m
Duration.Minutes(null)
```

```text
null
```

Minutes above 59 carry into the hours, so this returns 15 rather than 75.

```m
Duration.Minutes(#duration(0, 2, 75, 0))
```

```text
15
```

A whole number of hours has no leftover minutes, so this is 0 even though the duration holds 300 minutes.

```m
Duration.Minutes(#duration(0, 5, 0, 0))
```

```text
0
```

## Duration.Seconds

A null duration gives null.

```m
Duration.Seconds(null)
```

```text
null
```

Only the seconds component is returned, however large the other parts are.

```m
Duration.Seconds(#duration(2, 10, 30, 45))
```

```text
45
```

Seconds past a full minute are carried into the minutes first, so the result stays below 60.

```m
Duration.Seconds(#duration(0, 0, 0, 90))
```

```text
30
```

## Duration.ToRecord

These examples show how a duration splits into day, hour, minute and second parts, including carry-over, fractional seconds, and null, which is an error.

```m
Duration.ToRecord(#duration(0, 25, 0, 0))
```

```text
[Days = 1, Hours = 1, Minutes = 0, Seconds = 0]
```

```m
Duration.ToRecord(#duration(0, 0, 0, 1.5))
```

```text
[Days = 0, Hours = 0, Minutes = 0, Seconds = 1.5]
```

```m
Duration.ToRecord(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Duration. | Detail: [Value = null, Type = type duration]
```

## Duration.TotalDays

These examples show that a null propagates, that part of a day counts as a fraction, and that a negative duration yields a negative total.

```m
Duration.TotalDays(null)
```

```text
null
```

```m
Duration.TotalDays(#duration(0, 23, 59, 59))
```

```text
0.99998842592592585
```

```m
Duration.TotalDays(#duration(-2, -12, 0, 0))
```

```text
-2.5
```

## Duration.TotalHours

These examples show null handling and totals built from whole days or minutes rather than the hours component alone.

```m
Duration.TotalHours(null)
```

```text
null
```

```m
Duration.TotalHours(#duration(2, 3, 0, 0))
```

```text
51
```

```m
Duration.TotalHours(#duration(0, 0, 90, 0))
```

```text
1.5
```

## Duration.TotalMinutes

Nulls stay null, and total minutes include hours and fractions of a minute.

```m
Duration.TotalMinutes(null)
```

```text
null
```

```m
Duration.TotalMinutes(#duration(0, 1, 30, 0))
```

```text
90
```

```m
Duration.TotalMinutes(#duration(0, 0, 0, 30))
```

```text
0.5
```

## Duration.TotalSeconds

These examples show that fractions of a second are kept, that hours past a day still count, and that a null duration stays null.

```m
Duration.TotalSeconds(#duration(0, 0, 0, 1.5))
```

```text
1.5
```

```m
Duration.TotalSeconds(#duration(0, 25, 0, 0))
```

```text
90000
```

```m
Duration.TotalSeconds(null)
```

```text
null
```

## Duration.ToText

These examples show null propagation, a `format` argument that is now an error, and sub-day durations.

```m
Duration.ToText(null)
```

```text
null
```

```m
Duration.ToText(#duration(0, 5, 6, 7), null)
```

```text
"05:06:07"
```

```m
Duration.ToText(#duration(1, 2, 3, 4), "d.hh:mm:ss")
```

```text
error: Expression.Error: The "format" parameter of Duration.ToText has no effect and is no longer supported.
```
