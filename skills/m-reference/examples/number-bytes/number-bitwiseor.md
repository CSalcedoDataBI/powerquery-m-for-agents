<!-- lab: desktop 2.159.883.0 -->

# Number.BitwiseOr

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
