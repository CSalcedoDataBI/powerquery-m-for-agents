<!-- lab: desktop 2.159.883.0 -->

# Number.IsEven

Zero, negative and fractional numbers, null, and large values.

```m
List.Transform({0, -4, -3, 2.5, 4.0}, Number.IsEven)
```

```text
{true, true, false, true, true}
```

A null argument:

```m
Number.IsEven(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Number. | Detail: [Value = null, Type = type number]
```

Above 2^53 a double cannot hold every integer, so 1e16 + 1 is rounded before the parity check:

```m
List.Transform({1e16 + 1, Int64.From(9007199254740993)}, Number.IsEven)
```

```text
{true, true}
```
