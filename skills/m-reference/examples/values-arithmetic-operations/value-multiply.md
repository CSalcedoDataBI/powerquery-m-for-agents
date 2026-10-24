<!-- lab: desktop 2.159.883.0 -->

# Value.Multiply

A null on either side gives null, and the optional precision decides whether decimal fractions multiply exactly.

```m
{Value.Multiply(5, null), Value.Multiply(null, 2), Value.Multiply(null, null)}
```

```text
{null, null, null}
```

```m
{Value.Multiply(0.1, 3) = 0.3, Value.Multiply(0.1, 3, Precision.Double) = 0.3, Value.Multiply(0.1, 3, Precision.Decimal) = 0.3}
```

```text
{false, false, true}
```

```m
{Value.Multiply(#duration(0, 1, 30, 0), 3), Value.Multiply(2, #duration(1, 0, 0, 0))}
```

```text
{#duration(0, 4, 30, 0), #duration(2, 0, 0, 0)}
```
