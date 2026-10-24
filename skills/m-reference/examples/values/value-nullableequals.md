<!-- lab: desktop 2.159.883.0 -->

# Value.NullableEquals

A null on either side gives null, not false, even when both sides are null.

```m
{Value.NullableEquals(null, 1), Value.NullableEquals(null, null), Value.NullableEquals(1, 1), Value.NullableEquals(1, "1")}
```

```text
{null, null, true, false}
```

The optional precision decides whether a sum of doubles matches its decimal value.

```m
{Value.NullableEquals(0.1 + 0.2, 0.3), Value.NullableEquals(Value.Add(0.1, 0.2, Precision.Decimal), 0.3, Precision.Decimal)}
```

```text
{false, true}
```

Compare with Value.Equals, which treats two nulls as equal.

```m
{Value.Equals(null, null), Value.NullableEquals(null, null)}
```

```text
{true, null}
```
