<!-- lab: desktop 2.159.883.0 -->

# Value.Equals

These examples show how nulls, precision, mixed types and structured values compare.

```m
{Value.Equals(null, null), Value.Equals(null, 0), Value.Equals(null, ""), Value.Equals("a", "A")}
```

```text
{true, false, false, false}
```

The optional precision argument changes how numbers compare.

```m
{Value.Equals(0.1 + 0.2, 0.3), Value.Equals(0.1 + 0.2, 0.3, Precision.Double), Value.Equals(0.1 + 0.2, 0.3, Precision.Decimal)}
```

```text
{false, false, true}
```

Records compare by field name, but lists compare by item order. A date never equals a datetime.

```m
{Value.Equals([a = 1, b = 2], [b = 2, a = 1]), Value.Equals({1, 2}, {2, 1}), Value.Equals(#date(2020, 1, 1), #datetime(2020, 1, 1, 0, 0, 0)), Value.Equals(1, 1.0)}
```

```text
{true, false, false, true}
```
