<!-- lab: desktop 2.159.883.0 -->

# Number.Atan2

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
