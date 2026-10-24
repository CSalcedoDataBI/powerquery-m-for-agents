<!-- lab: desktop 2.159.883.0 -->

# Number.Sin

The argument is in radians, a null input returns null, and results at multiples of pi are not exactly zero.

```m
{Number.Sin(90), Number.Sin(Number.PI / 2), Number.Sin(90 * Number.PI / 180)}
```

```text
{0.89399666360055785, 1, 1}
```

A null input returns null instead of raising an error.

```m
Number.Sin(null)
```

```text
null
```

Number.PI is only an approximation of pi, so the sine of pi is a tiny number, not 0.

```m
{Number.Sin(Number.PI), Number.Sin(Number.PI) = 0, Number.Round(Number.Sin(Number.PI), 10)}
```

```text
{1.2246063538223773E-16, false, 0}
```
