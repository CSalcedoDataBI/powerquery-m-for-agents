<!-- lab: desktop 2.159.883.0 -->

# Executed examples: number-information

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Number.IsEven

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

## Number.IsNaN

Only undefined results such as 0/0 are NaN; infinities are not.

```m
{Number.IsNaN(Number.NaN), Number.IsNaN(0/0), Number.IsNaN(1/0), Number.IsNaN(-1/0), Number.IsNaN(0)}
```

```text
{true, true, false, false, false}
```

NaN is not equal to itself, so `=` cannot find it, but Number.IsNaN can.

```m
{Number.NaN = Number.NaN, Number.IsNaN(Number.NaN)}
```

```text
{false, true}
```

The parameter is not nullable.

```m
Number.IsNaN(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Number. | Detail: [Value = null, Type = type number]
```

## Number.IsOdd

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
