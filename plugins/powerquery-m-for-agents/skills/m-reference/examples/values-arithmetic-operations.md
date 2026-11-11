<!-- lab: desktop 2.159.883.0 -->

# Executed examples: values-arithmetic-operations

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Value.Add

The examples show that a null operand gives null, and that the optional precision argument changes the result of decimal sums.

```m
[WithNull = Value.Add(1, null), BothNull = Value.Add(null, null)]
```

```text
[WithNull = null, BothNull = null]
```

By default the sum uses double precision. Precision.Decimal gives exact decimal arithmetic.

```m
[Default = Value.Add(0.1, 0.2) = 0.3, Decimal = Value.Add(0.1, 0.2, Precision.Decimal) = 0.3]
```

```text
[Default = false, Decimal = true]
```

Value.Add also accepts non-numeric pairs that the + operator supports, such as a date plus a duration.

```m
Value.Add(#date(1990, 12, 31), #duration(1, 0, 0, 0))
```

```text
#date(1991, 1, 1)
```

## Value.Divide

A null operand gives null, dividing by zero does not raise an error, and the precision argument changes the digits you get back.

```m
[NullDivisor = Value.Divide(10, null), NullDividend = Value.Divide(null, 10), ByZero = Value.Divide(1, 0), NegativeByZero = Value.Divide(-1, 0), ZeroByZero = Value.Divide(0, 0)]
```

```text
[NullDivisor = null, NullDividend = null, ByZero = #infinity, NegativeByZero = -#infinity, ZeroByZero = #nan]
```

Precision.Double is the default. Precision.Decimal keeps more digits and may treat a zero divisor differently.

```m
[Default = Value.Divide(1, 3), Double = Value.Divide(1, 3, Precision.Double), Decimal = Value.Divide(1, 3, Precision.Decimal), DecimalByZero = Value.Divide(1, 0, Precision.Decimal)]
```

```text
[Default = 0.33333333333333331, Double = 0.33333333333333331, Decimal = 0.3333333333333333333333333333, DecimalByZero = #infinity]
```

Durations can be divided by numbers or by another duration.

```m
[HalfDay = Value.Divide(#duration(1, 0, 0, 0), 2), Ratio = Value.Divide(#duration(1, 0, 0, 0), #duration(0, 6, 0, 0))]
```

```text
[HalfDay = #duration(0, 12, 0, 0), Ratio = 4]
```

## Value.Multiply

A null on either side gives null, and the optional precision decides whether decimal fractions multiply exactly.

```m
{Value.Multiply(5, null), Value.Multiply(null, 2), Value.Multiply(null, null)}
```

```text
{null, null, null}
```

```m
{Value.Multiply(0.1, 3) = 0.3, Value.Multiply(0.1, 3, Precision.Double) = 0.3, Value.Multiply(0.1, 3, Precision.Decimal) = 0.3}
```

```text
{false, false, true}
```

```m
{Value.Multiply(#duration(0, 1, 30, 0), 3), Value.Multiply(2, #duration(1, 0, 0, 0))}
```

```text
{#duration(0, 4, 30, 0), #duration(2, 0, 0, 0)}
```

## Value.Subtract

The examples show how nulls, the optional precision argument and date values change the result.

A null on either side makes the result null.

```m
{Value.Subtract(5, null), Value.Subtract(null, 5)}
```

```text
{null, null}
```

The default double precision can leave a rounding error. Precision.Decimal subtracts exactly.

```m
{Value.Subtract(0.3, 0.1), Value.Subtract(0.3, 0.1, Precision.Decimal)}
```

```text
{0.19999999999999998, 0.2}
```

Subtracting two dates gives a duration. Subtracting a duration from a datetime gives a datetime.

```m
{Value.Subtract(#date(2200, 3, 1), #date(2200, 2, 1)), Value.Subtract(#datetime(1990, 1, 1, 0, 0, 0), #duration(0, 1, 0, 0))}
```

```text
{#duration(28, 0, 0, 0), #datetime(1989, 12, 31, 23, 0, 0)}
```
