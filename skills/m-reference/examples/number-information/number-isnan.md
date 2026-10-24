<!-- lab: desktop 2.159.883.0 -->

# Number.IsNaN

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
