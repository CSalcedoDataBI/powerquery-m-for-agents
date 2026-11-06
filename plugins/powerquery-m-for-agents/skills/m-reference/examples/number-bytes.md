<!-- lab: desktop 2.159.883.0 -->

# Executed examples: number-bytes

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Number.BitwiseAnd

The examples show the basic mask, how nulls propagate, and how negative and fractional inputs behave.

```m
[Mask = Number.BitwiseAnd(12, 10), LowByte = Number.BitwiseAnd(0x1234, 0xFF), WithZero = Number.BitwiseAnd(255, 0)]
```

```text
[Mask = 8, LowByte = 52, WithZero = 0]
```

A null on either side gives null instead of being treated as zero.

```m
[NullFirst = Number.BitwiseAnd(null, 7), NullSecond = Number.BitwiseAnd(7, null), BothNull = Number.BitwiseAnd(null, null)]
```

```text
[NullFirst = null, NullSecond = null, BothNull = null]
```

Negative numbers use two's complement, and fractional inputs are not plain integers.

```m
[NegativeMask = Number.BitwiseAnd(-1, 0xFF), NegativeBoth = Number.BitwiseAnd(-8, -3), Fraction = try Number.BitwiseAnd(5.7, 3) otherwise "error"]
```

```text
[NegativeMask = 255, NegativeBoth = -8, Fraction = "error"]
```

## Number.BitwiseNot

These blocks test whether the result really stays within one byte, as the description says, and how null and fractional inputs behave.

```m
{Number.BitwiseNot(0), Number.BitwiseNot(5), Number.BitwiseNot(255), Number.BitwiseNot(-1)}
```

```text
{-1, -6, -256, 0}
```

```m
{Number.BitwiseNot(null), Number.BitwiseNot(Number.BitwiseNot(5)), Number.BitwiseAnd(Number.BitwiseNot(5), 255)}
```

```text
{null, 5, 250}
```

```m
try Number.BitwiseNot(1.5)
```

```text
[HasError = true, Error = [Reason = "Expression.Error", Message = "The number is out of range of a 64 bit integer value.", Detail = 1.5, #"Message.Format" = "The number is out of range of a 64 bit integer value.", #"Message.Parameters" = null, ErrorCode = "10109"]]
```

## Number.BitwiseOr

A null on either side gives null, and negative or fractional inputs may not give what you expect.

```m
{Number.BitwiseOr(5, 3), Number.BitwiseOr(12, 10), Number.BitwiseOr(5, null), Number.BitwiseOr(null, 3)}
```

```text
{7, 14, null, null}
```

Negative numbers use two's complement, so the sign bit stays set.

```m
{Number.BitwiseOr(-8, 3), Number.BitwiseOr(-1, 0), Number.BitwiseOr(-16, 15)}
```

```text
{-5, -1, -1}
```

Fractional inputs are not integers.

```m
Number.BitwiseOr(5.7, 2)
```

```text
error: Expression.Error: The number is out of range of a 64 bit integer value. | Detail: 5.7
```

## Number.BitwiseShiftLeft

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

## Number.BitwiseShiftRight

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

## Number.BitwiseXor

The examples show XOR as a self-inverse operation and how it handles nulls, negative values and fractional values.

```m
[a = Number.BitwiseXor(12, 10), b = Number.BitwiseXor(Number.BitwiseXor(12, 10), 10), c = Number.BitwiseXor(7, 7)]
```

```text
[a = 6, b = 12, c = 0]
```

A null in either argument gives null rather than an error.

```m
[left = Number.BitwiseXor(null, 5), right = Number.BitwiseXor(5, null), both = Number.BitwiseXor(null, null)]
```

```text
[left = null, right = null, both = null]
```

Negative values and fractional values show how the inputs are converted to integers.

```m
[negOne = Number.BitwiseXor(-1, 5), negBoth = Number.BitwiseXor(-8, -3), frac = Number.BitwiseXor(5.7, 1), fracNeg = Number.BitwiseXor(-5.7, 1)]
```

```text
[negOne = -6, negBoth = 5, frac = error: Expression.Error: The number is out of range of a 64 bit integer value. | Detail: 5.7, fracNeg = error: Expression.Error: The number is out of range of a 64 bit integer value. | Detail: -5.7]
```
