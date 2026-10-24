<!-- lab: desktop 2.159.883.0 -->

# Number.IsOdd

These examples show how negative numbers, fractions and null are handled.

```m
{Number.IsOdd(3), Number.IsOdd(-3), Number.IsOdd(0), Number.IsOdd(-4)}
```

```text
{true, true, false, false}
```

A fraction is neither odd nor even, whatever integer it sits next to.

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
