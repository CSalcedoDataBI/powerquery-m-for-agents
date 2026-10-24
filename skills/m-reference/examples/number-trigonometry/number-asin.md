<!-- lab: desktop 2.159.883.0 -->

# Number.Asin

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
