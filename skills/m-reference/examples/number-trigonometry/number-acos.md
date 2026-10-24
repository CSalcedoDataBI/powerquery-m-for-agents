<!-- lab: desktop 2.159.883.0 -->

# Number.Acos

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
