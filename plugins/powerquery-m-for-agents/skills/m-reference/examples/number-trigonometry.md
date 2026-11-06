<!-- lab: desktop 2.159.883.0 -->

# Executed examples: number-trigonometry

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Number.Acos

Results are in radians, null passes through, and inputs outside -1 to 1 give NaN rather than an error.

```m
{Number.Acos(1), Number.Acos(0), Number.Acos(-1)}
```

```text
{0, 1.5707963267948966, 3.1415926535897931}
```

Null returns null. A value outside the domain returns NaN and does not raise an error.

```m
{Number.Acos(null), Number.Acos(2), Number.Acos(-1.0001)}
```

```text
{null, #nan, #nan}
```

To get degrees, convert the result yourself.

```m
Number.Acos(0.5) * 180 / Number.PI
```

```text
60.000000000000007
```

## Number.Asin

The result is in radians, null passes through, and inputs outside -1 to 1 give no error.

```m
{Number.Asin(1), Number.Asin(-1), Number.Asin(0.5), Number.Asin(1) * 180 / Number.PI}
```

```text
{1.5707963267948966, -1.5707963267948966, 0.52359877559829893, 90}
```

```m
{Number.Asin(null), Number.Asin(2), Number.Asin(-1.0000001)}
```

```text
{null, #nan, #nan}
```

```m
Number.Sin(Number.Asin(0.3))
```

```text
0.3
```

## Number.Atan

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

## Number.Atan2

These examples show the argument order (y first, then x), how the signs pick the quadrant compared with Number.Atan, and what happens with zero and null arguments.

```m
{Number.Atan2(1, -1), Number.Atan(1 / -1), Number.Atan2(-1, 1), Number.Atan2(-1, -1)}
```

```text
{2.3561944901923448, -0.78539816339744828, -0.78539816339744828, -2.3561944901923448}
```

```m
{Number.Atan2(1, 0), Number.Atan2(-1, 0), Number.Atan2(0, -1), Number.Atan2(0, 0)}
```

```text
{1.5707963267948966, -1.5707963267948966, 3.1415926535897931, 0}
```

```m
{Number.Atan2(null, 1), Number.Atan2(1, null), Number.Atan2(null, null)}
```

```text
{null, null, null}
```

## Number.Cos

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

## Number.Cosh

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

## Number.Sin

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

## Number.Sinh

Null passes through, the function is odd around zero, and large inputs overflow.

```m
Number.Sinh(null)
```

```text
null
```

```m
{Number.Sinh(0), Number.Sinh(1), Number.Sinh(-1)}
```

```text
{0, 1.1752011936438014, -1.1752011936438014}
```

```m
{Number.Sinh(709), Number.Sinh(711), Number.Sinh(-1000)}
```

```text
{4.1092037307774862E+307, #infinity, -#infinity}
```

## Number.Tan

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

## Number.Tanh

The examples show that tanh is odd, that null passes through, and how large or special inputs saturate at ±1.

```m
{Number.Tanh(0), Number.Tanh(1), Number.Tanh(-1), Number.Tanh(0.5)}
```

```text
{0, 0.76159415595576485, -0.76159415595576485, 0.46211715726000974}
```

```m
Number.Tanh(null)
```

```text
null
```

```m
{Number.Tanh(20), Number.Tanh(-1000), Number.Tanh(#infinity), Number.Tanh(-#infinity), Number.Tanh(Number.NaN)}
```

```text
{1, -1, 1, -1, #nan}
```
