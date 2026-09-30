<!-- lab: desktop 2.157.879.0 -->

# Number.Mod

The remainder takes the sign of the dividend.

```m
{Number.Mod(7, 3), Number.Mod(-7, 3), Number.Mod(7, -3)}
```

```text
{1, -1, 1}
```

Double against Decimal precision.

```m
{Number.Mod(10.5, 0.2), Number.Mod(10.5, 0.2, Precision.Decimal)}
```

```text
{0.099999999999999423, 0.1}
```

A zero divisor returns NaN, not an error.

```m
Number.Mod(5, 0)
```

```text
#nan
```
