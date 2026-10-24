<!-- lab: desktop 2.159.883.0 -->

# Number.Tan

The input is in radians, a null input returns null, and exact angles give floating-point approximations instead of round values.

```m
{Number.Tan(null), Number.Tan(0), Number.Tan(45), Number.Tan(45 * Number.PI / 180)}
```

```text
{null, 0, 1.6197751905438615, 0.99999999999999989}
```

```m
{Number.Tan(Number.PI / 4), Number.Tan(Number.PI / 2), Number.Tan(-Number.PI / 2), Number.Tan(Number.PI)}
```

```text
{0.99999999999999989, 16331778728383844, -16331778728383844, -1.2246063538223773E-16}
```

```m
{Number.Tan(Number.PositiveInfinity), Number.Tan(Number.NaN), Number.Tan(-0.5) = -Number.Tan(0.5)}
```

```text
{#nan, #nan, true}
```
