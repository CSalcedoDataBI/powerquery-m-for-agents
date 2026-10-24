<!-- lab: desktop 2.159.883.0 -->

# Value.Subtract

The examples show how nulls, the optional precision argument and date values change the result.

A null on either side makes the result null.

```m
{Value.Subtract(5, null), Value.Subtract(null, 5)}
```

```text
{null, null}
```

The default double precision can leave a rounding error. Precision.Decimal subtracts exactly.

```m
{Value.Subtract(0.3, 0.1), Value.Subtract(0.3, 0.1, Precision.Decimal)}
```

```text
{0.19999999999999998, 0.2}
```

Subtracting two dates gives a duration. Subtracting a duration from a datetime gives a datetime.

```m
{Value.Subtract(#date(2200, 3, 1), #date(2200, 2, 1)), Value.Subtract(#datetime(1990, 1, 1, 0, 0, 0), #duration(0, 1, 0, 0))}
```

```text
{#duration(28, 0, 0, 0), #datetime(1989, 12, 31, 23, 0, 0)}
```
