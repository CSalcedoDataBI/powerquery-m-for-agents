<!-- lab: desktop 2.159.883.0 -->

# Value.Add

The examples show that a null operand gives null, and that the optional precision argument changes the result of decimal sums.

```m
[WithNull = Value.Add(1, null), BothNull = Value.Add(null, null)]
```

```text
[WithNull = null, BothNull = null]
```

By default the sum uses double precision. Precision.Decimal gives exact decimal arithmetic.

```m
[Default = Value.Add(0.1, 0.2) = 0.3, Decimal = Value.Add(0.1, 0.2, Precision.Decimal) = 0.3]
```

```text
[Default = false, Decimal = true]
```

Value.Add also accepts non-numeric pairs that the + operator supports, such as a date plus a duration.

```m
Value.Add(#date(1990, 12, 31), #duration(1, 0, 0, 0))
```

```text
#date(1991, 1, 1)
```
