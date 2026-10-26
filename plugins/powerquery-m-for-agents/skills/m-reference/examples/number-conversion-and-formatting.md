<!-- lab: desktop 2.157.879.0 -->

# Executed examples: number-conversion-and-formatting

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Byte.From

Nulls pass through, and the default rounding of a fractional value is not the one you might expect.

```m
Byte.From(null)
```

```text
null
```

With no rounding mode, a fractional value rounds to the nearest even integer.

```m
Byte.From("4.5")
```

```text
4
```

Naming a rounding mode while leaving `culture` unset rounds the other way.

```m
Byte.From("4.5", null, RoundingMode.AwayFromZero)
```

```text
5
```

## Currency.From

These examples show null handling, default rounding, and an explicit rounding mode.

```m
Currency.From(null)
```

```text
null
```

```m
Currency.From("1.23445")
```

```text
1.23440
```

```m
Currency.From("1.23445", "en-US", RoundingMode.Up)
```

```text
1.23450
```

## Decimal.From

Null passes through, an explicit culture changes how text is parsed, and a value that is already a number is returned as-is.

```m
Decimal.From(null)
```

```text
null
```

```m
Decimal.From("1.234,5", "de-DE")
```

```text
1234.5
```

```m
Decimal.From(123)
```

```text
123
```

## Double.From

Nulls pass through, the optional culture changes how text is read, and a number past the Double range becomes infinity, not an error.

```m
Double.From(null)
```

```text
null
```

```m
Double.From("1,5", "fr-FR")
```

```text
1.5
```

```m
Double.From(Number.Power(2, 1024))
```

```text
#infinity
```

## Int16.From

Nulls pass through, fractional values round to even by default, and values outside the 16-bit range are rejected.

```m
Int16.From(null)
```

```text
null
```

```m
{Int16.From(2.5), Int16.From(3.5), Int16.From(2.5, null, RoundingMode.AwayFromZero)}
```

```text
{2, 4, 3}
```

```m
Int16.From(32768)
```

```text
error: Expression.Error: The number is out of range of a 16 bit integer value. | Detail: 32768
```

## Int32.From

The examples show that `null` passes straight through, that fractional numbers are rounded to even by default, and that an explicit rounding mode overrides it.

```m
Int32.From(null)
```

```text
null
```

```m
Int32.From(2.5)
```

```text
2
```

```m
Int32.From("4.5", null, RoundingMode.AwayFromZero)
```

```text
5
```

The rounding mode only breaks ties: 7.9 still becomes 8 with `RoundingMode.Down`.

```m
{Int32.From(7.9, null, RoundingMode.Down), Int32.From(-7.9, null, RoundingMode.TowardZero)}
```

```text
{8, -8}
```

## Int64.From

These examples show how `Int64.From` handles nulls, default banker's rounding, and culture-aware text conversion with an explicit rounding mode.

```m
Int64.From(null)
```

```text
null
```

```m
Int64.From(2.5)
```

```text
2
```

```m
Int64.From("4,5", "fr-FR", RoundingMode.AwayFromZero)
```

```text
5
```

## Int8.From

These examples show null input, the default banker's rounding, and an explicit rounding mode with a culture.

```m
Int8.From(null)
```

```text
null
```

```m
Int8.From("4.5")
```

```text
4
```

```m
Int8.From("1,5", "de-DE", RoundingMode.AwayFromZero)
```

```text
2
```

## Number.From

Null is preserved and the optional culture argument changes how text is read.

```m
Number.From(null)
```

```text
null
```

Culture changes the meaning of separators, so the same text parses differently.

```m
Number.From("1.234,56", "de-DE")
```

```text
1234.56
```

Logical, time, and duration values convert as well.

```m
List.Transform({true, false, #time(6, 0, 0), #duration(1, 12, 0, 0)}, Number.From)
```

```text
{1, 0, 0.25, 1.5}
```

## Number.FromText

Null text yields null, the optional culture changes how separators are read, and text without a valid number raises an error.

```m
Number.FromText(null)
```

```text
null
```

The culture argument is optional but decisive when a comma is involved.

```m
Number.FromText("1.234,5", "de-DE")
```

```text
1234.5
```

A string that does not hold a valid number fails instead of returning null.

```m
Number.FromText("12 apples")
```

```text
error: DataFormat.Error: We couldn't convert to Number. | Detail: "12 apples"
```

## Number.ToText

The examples show null handling, culture-sensitive separators, and standard format strings.

```m
Number.ToText(null)
```

```text
null
```

```m
Number.ToText(1234.5678, "N2", "de-DE")
```

```text
"1.234,57"
```

```m
[
    default = Number.ToText(4),
    exponential = Number.ToText(4, "e"),
    percent = Number.ToText(-0.1234, "P1", "en-US")
]
```

```text
[default = "4", exponential = "4.000000e+000", percent = "-12.3%"]
```

## Percentage.From

These examples show what happens with `null`, text that has no percent symbol, and the optional `culture` argument.

A `null` input returns `null` rather than an error.

```m
Percentage.From(null)
```

```text
null
```

Without a percent sign the text is read as a plain number: nothing is divided by 100.

```m
Percentage.From("12.3")
```

```text
12.3
```

Culture matters when the text uses a comma as the decimal separator.

```m
Percentage.From("12,3%", "de-DE")
```

```text
0.123
```

## Single.From

These examples show how `Single.From` handles `null`, the optional `culture` argument, and values outside the Single range.

```m
Single.From(null)
```

```text
null
```

```m
Single.From("1,5", "fr-FR")
```

```text
1.5
```

```m
Single.From(1E39)
```

```text
#infinity
```
