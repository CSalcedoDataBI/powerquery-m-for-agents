<!-- lab: desktop 2.159.883.0 -->

# Number.RoundDown

These examples show how negative numbers, the optional digits argument and nulls behave.

Negative numbers round toward negative infinity, not toward zero.

```m
{Number.RoundDown(1.7), Number.RoundDown(-1.2), Number.RoundDown(-1.7)}
```

```text
{1, -2, -2}
```

The digits argument sets decimal places. A negative value applies to the left of the decimal point.

```m
{Number.RoundDown(1.2345, 2), Number.RoundDown(-1.2345, 2), Number.RoundDown(1234.5, -2), Number.RoundDown(1.2345, 0)}
```

```text
{1.23, -1.24, 1200, 1}
```

A null number and a null digits argument behave differently.

```m
{Number.RoundDown(null), Number.RoundDown(null, 2), Number.RoundDown(1.789, null)}
```

```text
{null, null, 1}
```
