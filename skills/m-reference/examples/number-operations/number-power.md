<!-- lab: desktop 2.157.879.0 -->

# Number.Power

Integer, fractional and negative powers.

```m
{Number.Power(2, 10), Number.Power(9, 0.5), Number.Power(2, -1)}
```

```text
{1024, 3, 0.5}
```

A negative base with a fractional power is NaN, even when a real root exists.

```m
Number.Power(-8, 1/3)
```

```text
#nan
```
