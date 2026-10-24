<!-- lab: desktop 2.159.883.0 -->

# Number.BitwiseNot

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
