<!-- lab: desktop 2.159.883.0 -->

# Number.BitwiseXor

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
