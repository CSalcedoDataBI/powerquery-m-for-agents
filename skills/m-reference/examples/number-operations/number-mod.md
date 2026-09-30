<!-- lab: desktop 2.157.879.0 -->

# Number.Mod

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
