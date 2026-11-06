<!-- lab: desktop 2.159.883.0 -->

# Executed examples: values

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Value.Compare

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

## Value.Equals

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

## Value.NullableEquals

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

## Value.Type

A literal's type is the base kind only. Ascribed types come back unchanged, and the field types of a record literal are not inferred from their values.

```m
{Value.Type(1), Value.Type(1.5), Value.Type(null), Value.Type(#date(1990, 1, 1)), Value.Type("1")}
```

```text
{type number, type number, type null, type date, type text}
```

```m
Type.ListItem(Value.Type(Value.ReplaceType({1, 2}, type {number})))
```

```text
type number
```

```m
Type.RecordFields(Value.Type([A = 1, B = "x"]))
```

```text
[A = [Type = type any, Optional = false], B = [Type = type any, Optional = false]]
```
