<!-- lab: desktop 2.159.883.0 -->

# Number.BitwiseShiftLeft

These examples show basic left shifts, null arguments, and edge cases with negative, fractional and large inputs.

```m
[Basic = Number.BitwiseShiftLeft(1, 3), Zero = Number.BitwiseShiftLeft(5, 0), NullNumber = Number.BitwiseShiftLeft(null, 2), NullShift = Number.BitwiseShiftLeft(4, null)]
```

```text
[Basic = 8, Zero = 5, NullNumber = null, NullShift = null]
```

Negative values, negative shift counts and fractional inputs are less obvious.

```m
[NegativeValue = Number.BitwiseShiftLeft(-1, 4), NegativeShift = Number.BitwiseShiftLeft(16, -2), FractionalValue = Number.BitwiseShiftLeft(2.7, 1), FractionalShift = Number.BitwiseShiftLeft(1, 1.5)]
```

```text
[NegativeValue = -16, NegativeShift = 0, FractionalValue = error: Expression.Error: The number is out of range of a 64 bit integer value. | Detail: 2.7, FractionalShift = error: Expression.Error: The number is out of range of a 32 bit integer value. | Detail: 1.5]
```

Large shift counts show the integer width and overflow behaviour.

```m
[Shift31 = Number.BitwiseShiftLeft(1, 31), Shift32 = Number.BitwiseShiftLeft(1, 32), Shift63 = Number.BitwiseShiftLeft(1, 63), Shift64 = Number.BitwiseShiftLeft(1, 64)]
```

```text
[Shift31 = 2147483648, Shift32 = 4294967296, Shift63 = -9223372036854775808, Shift64 = 1]
```
