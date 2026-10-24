<!-- lab: desktop 2.159.883.0 -->

# Value.Divide

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
