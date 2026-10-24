<!-- lab: desktop 2.159.883.0 -->

# Number.BitwiseAnd

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
