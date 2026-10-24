<!-- lab: desktop 2.159.883.0 -->

# Number.Cosh

Null passes through, and the result is the same for a negative input.

```m
{Number.Cosh(null), Number.Cosh(0), Number.Cosh(1), Number.Cosh(-1)}
```

```text
{null, 1, 1.5430806348152437, 1.5430806348152437}
```

A large input stays finite near the largest double (710 gives about 1.1E+308); only an actually infinite input returns #infinity, and neither raises an error.

```m
{Number.Cosh(710), Number.Cosh(-710), Number.Cosh(Number.PositiveInfinity)}
```

```text
{1.1169973830808555E+308, 1.1169973830808555E+308, #infinity}
```

NaN propagates.

```m
Number.Cosh(Number.NaN)
```

```text
#nan
```
