<!-- lab: desktop 2.159.883.0 -->

# Number.IsOdd

These examples show how negative numbers, fractions and null are handled.

```m
{Number.IsOdd(3), Number.IsOdd(-3), Number.IsOdd(0), Number.IsOdd(-4)}
```

```text
{true, true, false, false}
```

The fractional part is dropped before the parity check, so 3.5 counts as odd (from 3), 2.5 as even (from 2) and 1.0000001 as odd (from 1).

```m
{Number.IsOdd(3.5), Number.IsOdd(2.5), Number.IsOdd(1.0000001)}
```

```text
{true, false, true}
```

The parameter is not nullable.

```m
Number.IsOdd(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Number. | Detail: [Value = null, Type = type number]
```
