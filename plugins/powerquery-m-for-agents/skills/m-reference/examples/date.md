<!-- lab: desktop 2.157.879.0 -->

# Executed examples: date

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Date.AddDays

Nulls propagate, negative counts move backwards across a month boundary, and the result keeps the input's type.

```m
Date.AddDays(null, 5)
```

```text
null
```

```m
Date.AddDays(#date(2011, 3, 1), -1)
```

```text
#date(2011, 2, 28)
```

```m
Date.AddDays(#datetime(2011, 5, 14, 23, 30, 0), 1)
```

```text
#datetime(2011, 5, 15, 23, 30, 0)
```

## Date.AddMonths

These examples show month-end clamping, negative month counts, and null input.

```m
Date.AddMonths(#date(1990, 1, 31), 1)
```

```text
#date(1990, 2, 28)
```

```m
Date.AddMonths(#datetimezone(2200, 3, 31, 8, 15, 22, 0, 0), -1)
```

```text
#datetimezone(2200, 2, 28, 8, 15, 22, 0, 0)
```

```m
Date.AddMonths(null, 5)
```

```text
null
```

## Date.AddQuarters

These examples show null propagation, end-of-month clamping, and a backward shift that keeps the time and offset.

```m
Date.AddQuarters(null, 4)
```

```text
null
```

```m
Date.AddQuarters(#date(2011, 11, 30), 1)
```

```text
#date(2012, 2, 29)
```

```m
Date.AddQuarters(#datetimezone(2200, 1, 31, 8, 15, 0, -5, 0), -1)
```

```text
#datetimezone(2199, 10, 31, 8, 15, 0, -5, 0)
```

## Date.AddWeeks

Adding weeks propagates nulls, preserves time and zone information, and accepts negative counts.

```m
Date.AddWeeks(null, 1)
```

```text
null
```

```m
Date.AddWeeks(#datetime(1990, 12, 31, 23, 59, 59), -2)
```

```text
#datetime(1990, 12, 17, 23, 59, 59)
```

```m
Date.AddWeeks(#datetimezone(2200, 1, 1, 0, 0, 0, 8, 0), 1)
```

```text
#datetimezone(2200, 1, 8, 0, 0, 0, 8, 0)
```

## Date.AddYears

Null input returns null.

```m
Date.AddYears(null, 4)
```

```text
null
```

A leap day clamps to the last day of February.

```m
Date.AddYears(#date(2016, 2, 29), 1)
```

```text
#date(2017, 2, 28)
```

A negative count subtracts years and preserves the time and offset.

```m
Date.AddYears(#datetimezone(1990, 5, 14, 8, 15, 22, 0, 0), -1)
```

```text
#datetimezone(1989, 5, 14, 8, 15, 22, 0, 0)
```

## Date.Day

The examples show the day component for null, a `datetime`, and a `datetimezone` value.

```m
Date.Day(null)
```

```text
null
```

A `datetime` reports its calendar day even one second before midnight.

```m
Date.Day(#datetime(1990, 1, 31, 23, 59, 59))
```

```text
31
```

A `datetimezone` reports the day in its stored local time, not the UTC instant.

```m
Date.Day(#datetimezone(2200, 12, 31, 23, 30, 0, -8, 0))
```

```text
31
```

## Date.DayOfWeek

The examples show how the optional first day of the week changes the numbering, that datetimezone values are accepted, and that null returns null.

```m
Date.DayOfWeek(#date(2011, 2, 21), Day.Monday)
```

```text
0
```

```m
Date.DayOfWeek(#datetimezone(2011, 2, 26, 23, 59, 59, 0, 0), Day.Sunday)
```

```text
6
```

```m
Date.DayOfWeek(null, Day.Sunday)
```

```text
null
```

## Date.DayOfWeekName

These examples show null propagation, the optional culture argument, and dates far from today.

```m
Date.DayOfWeekName(null)
```

```text
null
```

With no culture, the name comes from the query's culture: en-US in the lab model.

```m
Date.DayOfWeekName(#date(2200, 1, 1))
```

```text
"Wednesday"
```

A supplied culture changes the language of the name.

```m
Date.DayOfWeekName(#date(1990, 1, 1), "fr-FR")
```

```text
"lundi"
```

## Date.DayOfYear

The examples show how a null input is handled, how leap years affect the count, and how the time part of a value is ignored.

```m
Date.DayOfYear(null)
```

```text
null
```

A leap day sits at the same position as the March 1 of a common year.

```m
Date.DayOfYear(#date(2020, 2, 29))
```

```text
60
```

A `datetime` is accepted, and its time portion does not change the result.

```m
Date.DayOfYear(#datetime(2019, 3, 1, 23, 59, 59))
```

```text
60
```

## Date.DaysInMonth

Nulls give null, and February's length depends on whether the year is a leap year.

```m
Date.DaysInMonth(null)
```

```text
null
```

A leap year's February has 29 days.

```m
Date.DaysInMonth(#date(2020, 2, 1))
```

```text
29
```

A `datetime` value is accepted too, and 2200 is a century year that is not a leap year.

```m
Date.DaysInMonth(#datetime(2200, 2, 1, 12, 30, 0))
```

```text
28
```

## Date.EndOfDay

The examples show a `date` input, a `datetimezone` whose offset is preserved, and a null input.

```m
Date.EndOfDay(#date(2200, 1, 1))
```

```text
#date(2200, 1, 1)
```

```m
Date.EndOfDay(#datetimezone(1990, 12, 31, 23, 59, 59, -8, 0))
```

```text
#datetimezone(1990, 12, 31, 23, 59, 59.9999999, -8, 0)
```

```m
Date.EndOfDay(null)
```

```text
null
```

## Date.EndOfMonth

Null inputs, leap-year February, and the time component of a `datetime` are the cases most easily gotten wrong.

```m
Date.EndOfMonth(null)
```

```text
null
```

```m
Date.EndOfMonth(#date(2020, 2, 10))
```

```text
#date(2020, 2, 29)
```

```m
Date.EndOfMonth(#datetime(2011, 4, 7, 9, 30, 0))
```

```text
#datetime(2011, 4, 30, 23, 59, 59.9999999)
```

## Date.EndOfQuarter

The examples show a null input, a date on the first day of a quarter, and a datetimezone whose offset is preserved.

```m
Date.EndOfQuarter(null)
```

```text
null
```

```m
Date.EndOfQuarter(#date(2011, 1, 1))
```

```text
#date(2011, 3, 31)
```

```m
Date.EndOfQuarter(#datetimezone(2011, 10, 10, 8, 0, 0, 9, 30))
```

```text
#datetimezone(2011, 12, 31, 23, 59, 59.9999999, 9, 30)
```

## Date.EndOfWeek

These examples show null input, the default first day of the week, and an explicit first day with a timezone value.

A null date returns null.

```m
Date.EndOfWeek(null)
```

```text
null
```

With no first-day argument, the week starts on the culture's first day: Sunday for en-US, the culture the lab model sets.

```m
Date.EndOfWeek(#date(1990, 1, 1))
```

```text
#date(1990, 1, 6)
```

An explicit `Day.Monday` changes the week boundary, and a timezone value keeps its offset.

```m
Date.EndOfWeek(#datetimezone(2200, 1, 1, 5, 0, 0, -7, 0), Day.Monday)
```

```text
#datetimezone(2200, 1, 5, 23, 59, 59.9999999, -7, 0)
```

## Date.EndOfYear

A `date` argument keeps the `date` type.

```m
Date.EndOfYear(#date(1990, 3, 15))
```

```text
#date(1990, 12, 31)
```

Time zone information is preserved.

```m
Date.EndOfYear(#datetimezone(2200, 7, 4, 13, 45, 30, 5, 30))
```

```text
#datetimezone(2200, 12, 31, 23, 59, 59.9999999, 5, 30)
```

A `null` argument returns `null`.

```m
Date.EndOfYear(null)
```

```text
null
```

## Date.From

Nulls pass through, numeric serials use the 1899-12-30 base rather than Unix time, and the optional culture argument changes text parsing.

```m
Date.From(null)
```

```text
null
```

```m
Date.From(1.25)
```

```text
#date(1899, 12, 31)
```

```m
Date.From("20 Januar 2023", "de-DE")
```

```text
#date(2023, 1, 20)
```

## Date.FromText

The examples show a null input, the legacy culture-as-text option, and a format record for a non-Gregorian calendar.

```m
Date.FromText(null)
```

```text
null
```

```m
Date.FromText("01/02/2010", "en-GB")
```

```text
#date(2010, 2, 1)
```

```m
Date.FromText("1400", [Format = "yyyy", Culture = "ar-SA"])
```

```text
#date(1979, 11, 20)
```

## Date.IsInCurrentDay

Null propagates, there are no optional arguments, and far-future date and datetimezone values never fall in the current day.

```m
Date.IsInCurrentDay(null)
```

```text
null
```

```m
Date.IsInCurrentDay(#date(2200, 1, 1))
```

```text
false
```

```m
Date.IsInCurrentDay(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

## Date.IsInCurrentMonth

Nulls pass straight through, and dates far outside the current month return false however the block is run.

```m
Date.IsInCurrentMonth(null)
```

```text
null
```

```m
Date.IsInCurrentMonth(#date(1990, 1, 1))
```

```text
false
```

```m
Date.IsInCurrentMonth(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

## Date.IsInCurrentQuarter

Fixed dates far from the current quarter show which values qualify and how null is handled.

A date from 1990 never belongs to the current quarter.

```m
Date.IsInCurrentQuarter(#date(1990, 3, 15))
```

```text
false
```

A future value is not in the current quarter even when its quarter number lines up, because the year is not current.

```m
Date.IsInCurrentQuarter(#datetimezone(2200, 3, 15, 0, 0, 0, 0, 0))
```

```text
false
```

Null flows through instead of being treated as a date.

```m
Date.IsInCurrentQuarter(null)
```

```text
null
```

## Date.IsInCurrentWeek

A null argument and dates fixed in 1990 and 2200 show nullable handling and the relative-to-now check.

```m
Date.IsInCurrentWeek(null)
```

```text
null
```

```m
Date.IsInCurrentWeek(#date(1990, 1, 1))
```

```text
false
```

```m
Date.IsInCurrentWeek(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

## Date.IsInCurrentYear

These examples test how a null value and dates far outside the current year behave.

```m
Date.IsInCurrentYear(null)
```

```text
null
```

```m
Date.IsInCurrentYear(#date(1990, 3, 15))
```

```text
false
```

```m
Date.IsInCurrentYear(#datetime(2200, 12, 31, 23, 59, 59))
```

```text
false
```

## Date.IsInNextDay

Null propagates, and a value far from the current system day can never be the next day.

```m
Date.IsInNextDay(null)
```

```text
null
```

```m
Date.IsInNextDay(#date(2200, 1, 1))
```

```text
false
```

```m
Date.IsInNextDay(#datetime(1990, 12, 31, 23, 59, 59))
```

```text
false
```

## Date.IsInNextMonth

Nulls return null, and a date far from the current month is never in the next month.

```m
Date.IsInNextMonth(null)
```

```text
null
```

```m
Date.IsInNextMonth(#date(2200, 1, 15))
```

```text
false
```

```m
Date.IsInNextMonth(#datetimezone(1990, 12, 31, 23, 59, 59, -8, 0))
```

```text
false
```

## Date.IsInNextNDays

Null input returns null, past dates fall outside the window, and a large day count can still reach a far-future date.

```m
Date.IsInNextNDays(null, 2)
```

```text
null
```

```m
Date.IsInNextNDays(#date(1990, 1, 1), 2)
```

```text
false
```

```m
Date.IsInNextNDays(#date(2200, 1, 1), 100000)
```

```text
true
```

## Date.IsInNextNMonths

The examples cover null input, zero months, and fixed dates far from the current month.

A null date is accepted as input.

```m
Date.IsInNextNMonths(null, 1)
```

```text
null
```

A zero-month window does not match any month, even one far in the past.

```m
Date.IsInNextNMonths(#date(1990, 1, 1), 0)
```

```text
false
```

A fixed date far in the future stays outside the next month.

```m
Date.IsInNextNMonths(#date(2200, 1, 1), 1)
```

```text
false
```

## Date.IsInNextNQuarters

The examples show null handling, a past date, and a count large enough to reach a far-future date.

```m
Date.IsInNextNQuarters(null, 1)
```

```text
null
```

```m
Date.IsInNextNQuarters(#date(1990, 1, 1), 1000)
```

```text
false
```

```m
Date.IsInNextNQuarters(#date(2200, 6, 15), 1000)
```

```text
true
```

## Date.IsInNextNWeeks

Nulls pass through instead of becoming false.

```m
Date.IsInNextNWeeks(null, 2)
```

```text
null
```

A date far in the future is outside the next two weeks.

```m
Date.IsInNextNWeeks(#date(2200, 1, 1), 2)
```

```text
false
```

The current week is excluded, so a zero-week window matches no date.

```m
Date.IsInNextNWeeks(#date(1990, 1, 1), 0)
```

```text
false
```

## Date.IsInNextNYears

The examples show null handling and how fixed dates far from today are judged against a wide year window.

```m
Date.IsInNextNYears(null, 2)
```

```text
null
```

A far-future date lies inside a wide enough window no matter when the block runs.

```m
Date.IsInNextNYears(#date(2200, 6, 1), 1000)
```

```text
true
```

A past date is never in a future window, however many years it spans.

```m
Date.IsInNextNYears(#date(1990, 6, 1), 1000)
```

```text
false
```

## Date.IsInNextQuarter

Far-off dates and nulls show what "next quarter" does and does not include.

A null input yields null rather than false.

```m
Date.IsInNextQuarter(null)
```

```text
null
```

A date decades in the past is not in the next quarter.

```m
Date.IsInNextQuarter(#date(1990, 3, 15))
```

```text
false
```

A date far in the future is still not the *next* quarter, because "next" means the quarter immediately after the current one.

```m
Date.IsInNextQuarter(#datetime(2200, 6, 1, 0, 0, 0))
```

```text
false
```

## Date.IsInNextWeek

Distant dates fall outside the next week, and null input is passed through.

```m
Date.IsInNextWeek(#date(1990, 1, 1))
```

```text
false
```

A far-future datetime is outside the next week as well.

```m
Date.IsInNextWeek(#datetime(2200, 1, 1, 12, 0, 0))
```

```text
false
```

A null date shows how a missing value is handled.

```m
Date.IsInNextWeek(null)
```

```text
null
```

## Date.IsInNextYear

Fixed dates from opposite ends of the calendar show that the function compares against the current year, and null shows its null handling.

```m
Date.IsInNextYear(#date(1990, 12, 31))
```

```text
false
```

```m
Date.IsInNextYear(#date(2200, 1, 1))
```

```text
false
```

```m
Date.IsInNextYear(null)
```

```text
null
```

## Date.IsInPreviousDay

Null and fixed literal values show how this current-day test behaves when the input cannot be the previous day.

```m
Date.IsInPreviousDay(null)
```

```text
null
```

```m
Date.IsInPreviousDay(#date(1990, 1, 1))
```

```text
false
```

```m
Date.IsInPreviousDay(#datetimezone(2200, 6, 15, 8, 30, 0, -5, 0))
```

```text
false
```

## Date.IsInPreviousMonth

These examples show null handling and how dates fixed far from the system's clock behave.

A null input produces a null result rather than an error.

```m
Date.IsInPreviousMonth(null)
```

```text
null
```

A fixed 1990 date can never be the month before the current system month, whatever day the block runs.

```m
Date.IsInPreviousMonth(#date(1990, 1, 15))
```

```text
false
```

A `datetimezone` far in the future is likewise outside the previous month.

```m
Date.IsInPreviousMonth(#datetimezone(2200, 6, 1, 0, 0, 0, 0, 0))
```

```text
false
```

## Date.IsInPreviousNDays

A null input yields null, while dates far in the past or future never fall in a previous-day window.

```m
Date.IsInPreviousNDays(null, 2)
```

```text
null
```

A date centuries before the current day is not in the previous two days.

```m
Date.IsInPreviousNDays(#date(1990, 1, 1), 2)
```

```text
false
```

A future datetime is never in a previous window.

```m
Date.IsInPreviousNDays(#datetime(2200, 1, 1, 0, 0, 0), 1)
```

```text
false
```

## Date.IsInPreviousNMonths

These examples show null propagation, a zero-month window, and a far-off value that never lands in the previous months.

```m
Date.IsInPreviousNMonths(null, 3)
```

```text
null
```

```m
Date.IsInPreviousNMonths(#date(1990, 6, 15), 0)
```

```text
false
```

```m
Date.IsInPreviousNMonths(#datetime(2200, 1, 1, 12, 0, 0), 5)
```

```text
false
```

## Date.IsInPreviousNQuarters

The examples show null input, a far-past datetime, and a zero-quarter count.

```m
Date.IsInPreviousNQuarters(null, 4)
```

```text
null
```

```m
Date.IsInPreviousNQuarters(#datetime(1990, 1, 1, 0, 0, 0), 4)
```

```text
false
```

```m
Date.IsInPreviousNQuarters(#date(2200, 1, 1), 0)
```

```text
false
```

## Date.IsInPreviousNWeeks

Fixed dates far from the current week never qualify, and null passes through.

```m
Date.IsInPreviousNWeeks(#date(1990, 1, 1), 2)
```

```text
false
```

```m
Date.IsInPreviousNWeeks(#datetime(2200, 1, 1, 0, 0, 0), 1)
```

```text
false
```

```m
Date.IsInPreviousNWeeks(null, 2)
```

```text
null
```

## Date.IsInPreviousNYears

Nulls stay null, and the window looks only backward, so future dates never qualify.

```m
Date.IsInPreviousNYears(null, 2)
```

```text
null
```

A far-future date is never part of the previous years, however wide the count.

```m
Date.IsInPreviousNYears(#date(2200, 12, 31), 1000)
```

```text
false
```

A far-past date falls inside a large enough count.

```m
Date.IsInPreviousNYears(#date(1990, 1, 1), 1000)
```

```text
true
```

## Date.IsInPreviousQuarter

The previous quarter is measured from the current system date, so fixed literal dates are never in it.

```m
Date.IsInPreviousQuarter(#date(1990, 3, 14))
```

```text
false
```

A future `datetimezone` is accepted but is not the previous quarter.

```m
Date.IsInPreviousQuarter(#datetimezone(2200, 9, 1, 0, 0, 0, 0, 0))
```

```text
false
```

A `null` value gives `null`, not `false`.

```m
Date.IsInPreviousQuarter(null)
```

```text
null
```

## Date.IsInPreviousWeek

Fixed dates far from the current system week both return false, while a null argument propagates as null.

```m
Date.IsInPreviousWeek(#date(1990, 1, 1))
```

```text
false
```

```m
Date.IsInPreviousWeek(null)
```

```text
null
```

```m
Date.IsInPreviousWeek(#datetimezone(2200, 1, 1, 0, 0, 0, 0, 0))
```

```text
false
```

## Date.IsInPreviousYear

Nulls pass through, and fixed past or future dates are not the previous year.

```m
Date.IsInPreviousYear(null)
```

```text
null
```

```m
Date.IsInPreviousYear(#date(1990, 12, 31))
```

```text
false
```

```m
Date.IsInPreviousYear(#date(2200, 1, 1))
```

```text
false
```

## Date.IsInYearToDate

A null value gives null, and dates outside the current year give false whatever the current day is.

```m
Date.IsInYearToDate(null)
```

```text
null
```

A year that is not the current year falls outside the year to date, whether it is long past or far ahead.

```m
Date.IsInYearToDate(#date(1990, 6, 15))
```

```text
false
```

The argument is typed `any`, so a `datetimezone` value is accepted as well as a `date`.

```m
Date.IsInYearToDate(#datetimezone(2200, 6, 15, 10, 30, 0, 0, 0))
```

```text
false
```

## Date.IsLeapYear

These examples show null handling, the century rule, and a `datetime` argument.

```m
Date.IsLeapYear(null)
```

```text
null
```

A century year divisible by 4 but not 400 is not a leap year.

```m
Date.IsLeapYear(#date(1900, 1, 1))
```

```text
false
```

A `datetime` value is evaluated the same way, and 2000 is a leap year.

```m
Date.IsLeapYear(#datetime(2000, 1, 1, 0, 0, 0))
```

```text
true
```

## Date.Month

Null passes through, and the time part of a datetime does not affect the month.

```m
Date.Month(null)
```

```text
null
```

The last instant of a year still yields that year's month.

```m
Date.Month(#datetime(1990, 12, 31, 23, 59, 59))
```

```text
12
```

The month is taken from the value it is given, even after date arithmetic.

```m
Date.Month(Date.AddMonths(#date(2200, 1, 15), -1))
```

```text
12
```

## Date.MonthName

Null dates return null, the culture argument is optional, and datetime values are accepted. Without the argument the result follows the query's culture: these results are for en-US, the culture the lab model sets.

```m
Date.MonthName(null)
```

```text
null
```

```m
Date.MonthName(#date(2200, 2, 1))
```

```text
"February"
```

```m
Date.MonthName(#datetime(1990, 12, 31, 23, 59, 59), "fr-FR")
```

```text
"décembre"
```

## Date.QuarterOfYear

These examples show which quarter a date falls into at the March/April boundary, plus how null and datetime inputs behave.

Null input returns null.

```m
Date.QuarterOfYear(null)
```

```text
null
```

The last day of March is still quarter 1, while the first day of April is quarter 2.

```m
Date.QuarterOfYear(#date(2011, 3, 31))
```

```text
1
```

```m
Date.QuarterOfYear(#date(2011, 4, 1))
```

```text
2
```

A datetime value is judged by its date part, so the end of December is quarter 4.

```m
Date.QuarterOfYear(#datetime(1990, 12, 31, 23, 59, 59))
```

```text
4
```

## Date.StartOfDay

These examples show what Date.StartOfDay returns for null, a datetime, and a datetimezone value.

Passing null returns null instead of raising an error.

```m
Date.StartOfDay(null)
```

```text
null
```

A datetime keeps its date but drops the time, even from the last moment of the day.

```m
Date.StartOfDay(#datetime(2200, 3, 15, 23, 59, 59.999))
```

```text
#datetime(2200, 3, 15, 0, 0, 0)
```

A datetimezone resets the clock but preserves the original offset rather than converting to UTC.

```m
Date.StartOfDay(#datetimezone(1990, 12, 31, 18, 45, 0, -8, 0))
```

```text
#datetimezone(1990, 12, 31, 0, 0, 0, -8, 0)
```

## Date.StartOfMonth

The result keeps the input's type: a date stays a date, a datetime truncates to midnight.

```m
Date.StartOfMonth(#date(2011, 10, 10))
```

```text
#date(2011, 10, 1)
```

```m
Date.StartOfMonth(#datetime(1990, 2, 15, 8, 10, 32))
```

```text
#datetime(1990, 2, 1, 0, 0, 0)
```

```m
Date.StartOfMonth(null)
```

```text
null
```

## Date.StartOfQuarter

These examples show null handling and which parts of a `datetime` or `datetimezone` survive.

```m
Date.StartOfQuarter(null)
```

```text
null
```

```m
Date.StartOfQuarter(#datetime(2200, 2, 15, 13, 45, 0))
```

```text
#datetime(2200, 1, 1, 0, 0, 0)
```

```m
Date.StartOfQuarter(#datetimezone(1990, 12, 31, 23, 59, 59, 8, 0))
```

```text
#datetimezone(1990, 10, 1, 0, 0, 0, 8, 0)
```

## Date.StartOfWeek

The examples show null handling, the default Sunday start, and how the optional first day of week changes it. Without the argument the result follows the query's culture: these results are for en-US, the culture the lab model sets.

```m
Date.StartOfWeek(null)
```

```text
null
```

```m
Date.StartOfWeek(#datetimezone(1990, 10, 11, 8, 10, 32, 8, 0))
```

```text
#datetimezone(1990, 10, 7, 0, 0, 0, 8, 0)
```

```m
Date.StartOfWeek(#date(2200, 10, 11), Day.Monday)
```

```text
#date(2200, 10, 6)
```

## Date.StartOfYear

Nulls pass through, while date, datetime, and datetimezone inputs return the first instant of their year in the same type.

```m
Date.StartOfYear(null)
```

```text
null
```

A `datetime` keeps its type, dropping the time portion; this 2011 value is far enough from any run date to stay stable.

```m
Date.StartOfYear(#datetime(2011, 10, 10, 8, 10, 32))
```

```text
#datetime(2011, 1, 1, 0, 0, 0)
```

A `datetimezone` also keeps its offset, so year boundaries can shift relative to UTC.

```m
Date.StartOfYear(#datetimezone(2200, 12, 31, 23, 59, 59, 5, 30))
```

```text
#datetimezone(2200, 1, 1, 0, 0, 0, 5, 30)
```

## Date.ToRecord

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

## Date.ToText

These examples show how `Date.ToText` handles a null date, custom format and culture options, and the legacy text form of the options argument.

```m
Date.ToText(null)
```

```text
null
```

```m
Date.ToText(#date(2200, 1, 5), [Format = "dddd, dd MMMM yyyy", Culture = "fr-FR"])
```

```text
"dimanche, 05 janvier 2200"
```

```m
Date.ToText(#date(1990, 3, 1), "yyyy-MM-dd")
```

```text
"1990-03-01"
```

## Date.WeekOfMonth

Nulls pass through, and the optional first day of the week changes which week a date lands in. Without the argument the result follows the query's culture: these results are for en-US, the culture the lab model sets.

```m
Date.WeekOfMonth(null)
```

```text
null
```

```m
Date.WeekOfMonth(#date(2011, 3, 6))
```

```text
2
```

```m
Date.WeekOfMonth(#date(2011, 3, 6), Day.Monday)
```

```text
1
```

## Date.WeekOfYear

Null input returns null, and the start-of-week argument is accepted; for 1 January 2006 both starts give week 1.

```m
Date.WeekOfYear(null)
```

```text
null
```

```m
Date.WeekOfYear(#date(2006, 1, 1), Day.Sunday)
```

```text
1
```

```m
Date.WeekOfYear(#date(2006, 1, 1), Day.Monday)
```

```text
1
```

## Date.Year

These examples show the year for null, datetime and datetimezone values.

A null input returns null.

```m
Date.Year(null)
```

```text
null
```

The time part of a datetime does not affect the year.

```m
Date.Year(#datetime(1990, 12, 31, 23, 59, 59))
```

```text
1990
```

A datetimezone value is accepted, and its local date determines the year.

```m
Date.Year(#datetimezone(2200, 6, 15, 12, 30, 0, -8, 0))
```

```text
2200
```

## Time.EndOfHour

These examples show how nulls, time-only values, and a non-UTC zone offset are handled.

```m
Time.EndOfHour(null)
```

```text
null
```

```m
Time.EndOfHour(#time(5, 0, 0))
```

```text
#time(5, 59, 59.9999999)
```

```m
Time.EndOfHour(#datetimezone(2200, 1, 1, 0, 0, 0, 5, 30))
```

```text
#datetimezone(2200, 1, 1, 0, 59, 59.9999999, 5, 30)
```

## Time.StartOfHour

The reset keeps the input's type (and a datetimezone's offset) and passes null through.

```m
Time.StartOfHour(#time(8, 10, 32))
```

```text
#time(8, 0, 0)
```

```m
Time.StartOfHour(#datetimezone(2200, 6, 15, 14, 45, 30, 5, 30))
```

```text
#datetimezone(2200, 6, 15, 14, 0, 0, 5, 30)
```

```m
Time.StartOfHour(null)
```

```text
null
```
