<!-- lab: desktop 2.157.879.0 -->

# Number.IntegerDivide

Nulls propagate, negative dividends keep only the integer portion, and the optional third argument takes `Precision.Double` or `Precision.Decimal`.

```m
Number.IntegerDivide(null, 4)
```

```text
null
```

```m
Number.IntegerDivide(-7, 2)
```

```text
-3
```

```m
Number.IntegerDivide(10.5, 0.2, Precision.Decimal)
```

```text
52
```

Dividing by zero returns NaN, not an error.

```m
Number.IntegerDivide(7, 0)
```

```text
#nan
```
