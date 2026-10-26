<!-- lab: desktop 2.157.879.0 -->

# Executed examples: number-operations

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Number.Abs

Nulls stay null, and zero or already-positive values come back unchanged.

```m
Number.Abs(-3.5)
```

```text
3.5
```

```m
Number.Abs(null)
```

```text
null
```

```m
Number.Abs(0) + Number.Abs(4)
```

```text
4
```

## Number.Combinations

The examples show null arguments and the boundary case of choosing no items.

```m
Number.Combinations(null, 3)
```

```text
null
```

```m
Number.Combinations(5, null)
```

```text
null
```

```m
Number.Combinations(5, 0)
```

```text
1
```

A subset larger than the set is zero ways, not an error.

```m
Number.Combinations(2, 3)
```

```text
0
```

## Number.Exp

Nulls stay null, zero returns exactly 1, and very negative inputs underflow toward 0.

```m
Number.Exp(null)
```

```text
null
```

```m
Number.Exp(0)
```

```text
1
```

```m
Number.Exp(-1000)
```

```text
0
```

## Number.Factorial

Null passes through unchanged, zero is its own factorial, and results grow quickly.

```m
Number.Factorial(null)
```

```text
null
```

```m
Number.Factorial(0)
```

```text
1
```

```m
Number.Factorial(5)
```

```text
120
```

## Number.IntegerDivide

Nulls propagate, negative dividends keep only the integer portion, and the optional third argument takes `Precision.Double` or `Precision.Decimal`.

```m
Number.IntegerDivide(null, 4)
```

```text
null
```

```m
Number.IntegerDivide(-7, 2)
```

```text
-3
```

```m
Number.IntegerDivide(10.5, 0.2, Precision.Decimal)
```

```text
52
```

Dividing by zero returns NaN, not an error.

```m
Number.IntegerDivide(7, 0)
```

```text
#nan
```

## Number.Ln

These examples show null handling and the boundary values where the natural logarithm stops returning an ordinary number.

```m
Number.Ln(null)
```

```text
null
```

```m
List.Transform({0, 1, Number.E}, Number.Ln)
```

```text
{-#infinity, 0, 1}
```

```m
Number.Ln(-1)
```

```text
#nan
```

## Number.Log

These examples show the default base, an explicit base, and how a null input is handled.

```m
Number.Log(2)
```

```text
0.69314718055994529
```

```m
Number.Log(2, 10)
```

```text
0.3010299956639812
```

```m
Number.Log(null, 10)
```

```text
null
```

## Number.Log10

Nulls pass through unchanged, while zero and negative inputs expose the logarithm's boundary behaviour.

```m
Number.Log10(null)
```

```text
null
```

```m
Number.Log10(0)
```

```text
-#infinity
```

```m
Number.Log10(-1)
```

```text
#nan
```

## Number.Mod

The examples show how nulls, the optional precision argument, and negative or zero divisors behave.

A null dividend or divisor propagates instead of being treated as zero.

```m
[
    NullDividend = Number.Mod(null, 3),
    NullDivisor = Number.Mod(5, null)
]
```

```text
[NullDividend = null, NullDivisor = null]
```

The optional third argument switches between double and decimal arithmetic, which changes the decimal expansion of the remainder.

```m
let
    Dividend = 10.5,
    Divisor = 0.2
in
    [
        DoublePrecision = Number.ToText(Number.Mod(Dividend, Divisor, Precision.Double), "G"),
        DecimalPrecision = Number.ToText(Number.Mod(Dividend, Divisor, Precision.Decimal), "G")
    ]
```

```text
[DoublePrecision = "0.0999999999999994", DecimalPrecision = "0.1"]
```

The sign of the remainder follows the dividend, and a zero divisor is its own edge case.

```m
[
    NegativeDividend = Number.Mod(-5, 3),
    NegativeDivisor = Number.Mod(5, -3),
    ZeroDivisor = Number.Mod(5, 0)
]
```

```text
[NegativeDividend = -2, NegativeDivisor = 2, ZeroDivisor = #nan]
```

## Number.Permutations

Null arguments propagate, and a zero permutation size is a valid edge case.

```m
Number.Permutations(null, 3)
```

```text
null
```

```m
Number.Permutations(5, null)
```

```text
null
```

```m
Number.Permutations(5, 0)
```

```text
1
```

## Number.Power

The examples show null propagation, negative exponents, and a negative base raised to a fractional power.

```m
Number.Power(2, null)
```

```text
null
```

```m
Number.Power(2, -3)
```

```text
0.125
```

```m
Number.Power(-8, 1 / 3)
```

```text
#nan
```

## Number.Sign

Nulls propagate, zero is its own sign, and a list keeps both behaviours.

```m
Number.Sign(null)
```

```text
null
```

```m
Number.Sign(-0.0)
```

```text
0
```

```m
List.Transform({-2.5, 0, 7, null}, Number.Sign)
```

```text
{-1, 0, 1, null}
```

## Number.Sqrt

The examples show null input, a negative input, and a non-perfect square.

```m
Number.Sqrt(null)
```

```text
null
```

```m
Number.Sqrt(-16)
```

```text
#nan
```

```m
Number.Sqrt(85)
```

```text
9.2195444572928871
```
