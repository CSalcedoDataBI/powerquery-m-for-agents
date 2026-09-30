<!-- lab: desktop 2.157.879.0 -->

# Number.IntegerDivide

The fraction is dropped, including for negatives.

```m
{Number.IntegerDivide(7, 2), Number.IntegerDivide(-7, 2), Number.IntegerDivide(7, -2)}
```

```text
{3, -3, -3}
```

Dividing by zero returns NaN, not an error.

```m
Number.IntegerDivide(7, 0)
```

```text
#nan
```
