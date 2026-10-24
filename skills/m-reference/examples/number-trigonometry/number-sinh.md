<!-- lab: desktop 2.159.883.0 -->

# Number.Sinh

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
