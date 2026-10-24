<!-- lab: desktop 2.159.883.0 -->

# Number.BitwiseShiftRight

These examples show how bits fall off the right, how negative numbers and large shifts behave, and what a null in either argument returns.

```m
[Exact = Number.BitwiseShiftRight(16, 2), LowBitsDropped = Number.BitwiseShiftRight(7, 1), ByZero = Number.BitwiseShiftRight(5, 0)]
```

```text
[Exact = 4, LowBitsDropped = 3, ByZero = 5]
```

Negative numbers and shift counts at or past 64 bits can be surprising.

```m
[NegativeValue = Number.BitwiseShiftRight(-16, 2), MinusOne = Number.BitwiseShiftRight(-1, 1), Shift64 = Number.BitwiseShiftRight(256, 64), Shift65 = Number.BitwiseShiftRight(256, 65)]
```

```text
[NegativeValue = -4, MinusOne = -1, Shift64 = 256, Shift65 = 128]
```

A null in either argument gives null, not an error.

```m
[NullValue = Number.BitwiseShiftRight(null, 2), NullShift = Number.BitwiseShiftRight(16, null)]
```

```text
[NullValue = null, NullShift = null]
```
