<!-- lab: desktop 2.159.883.0 -->

# Number.Atan

The result is in radians, a null input gives null, and infinite inputs give a finite angle.

```m
{Number.Atan(1), Number.PI / 4, Number.Atan(null)}
```

```text
{0.78539816339744828, 0.78539816339744828, null}
```

Infinite inputs give plus or minus pi/2. NaN gives NaN.

```m
{Number.Atan(Number.PositiveInfinity), Number.Atan(Number.NegativeInfinity), Number.Atan(Number.NaN)}
```

```text
{1.5707963267948966, -1.5707963267948966, #nan}
```

To get degrees, convert the result yourself.

```m
Number.Atan(1) * 180 / Number.PI
```

```text
45
```
