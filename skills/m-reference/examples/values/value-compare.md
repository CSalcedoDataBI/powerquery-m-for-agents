<!-- lab: desktop 2.159.883.0 -->

# Value.Compare

The examples show how Value.Compare handles nulls, text case, numeric precision and mixed types.

Nulls take part in the ordering, and text is compared by character code, not alphabetically.

```m
{Value.Compare(null, 0), Value.Compare(null, null), Value.Compare("a", "B")}
```

```text
{-1, 0, 1}
```

The optional precision argument changes whether a tiny floating-point difference counts.

```m
{Value.Compare(0.1 + 0.2, 0.3), Value.Compare(0.1 + 0.2, 0.3, Precision.Double), Value.Compare(0.1 + 0.2, 0.3, Precision.Decimal)}
```

```text
{1, 1, 0}
```

Values of different types still get an ordering.

```m
{Value.Compare(1, "1"), Value.Compare(#date(1990, 1, 1), #datetime(1990, 1, 1, 0, 0, 0)), Value.Compare(true, 1)}
```

```text
{-1, -1, 1}
```
