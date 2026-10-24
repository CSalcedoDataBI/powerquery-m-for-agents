<!-- lab: desktop 2.159.883.0 -->

# Number.Cos

The argument is in radians, a null input returns null, and results at "exact" angles carry floating-point error.

```m
[Degrees60 = Number.Cos(60), Radians60 = Number.Cos(Number.PI / 3), Converted = Number.Cos(60 * Number.PI / 180)]
```

```text
[Degrees60 = -0.95241298041515632, Radians60 = 0.50000000000000011, Converted = 0.50000000000000011]
```

```m
{Number.Cos(null), Number.Cos(0), Number.Cos(Number.PI)}
```

```text
{null, 1, -1}
```

```m
[HalfPi = Number.Cos(Number.PI / 2), IsZero = Number.Cos(Number.PI / 2) = 0, Rounded = Number.Round(Number.Cos(Number.PI / 2), 10)]
```

```text
[HalfPi = 6.1230317691118863E-17, IsZero = false, Rounded = 0]
```
