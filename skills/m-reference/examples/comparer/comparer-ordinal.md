<!-- lab: desktop 2.159.883.0 -->

# Comparer.Ordinal

Called directly, it returns -1, 0 or 1, and it compares text by character code, so case matters.

```m
{Comparer.Ordinal("a", "A"), Comparer.Ordinal("A", "a"), Comparer.Ordinal("a", "a"), Comparer.Ordinal("Z", "a")}
```

```text
{1, -1, 0, -1}
```

As a sort comparer, all uppercase letters come before all lowercase letters. It does not sort alphabetically by letter.

```m
List.Sort({"b", "B", "a", "A", "Z", "z"}, Comparer.Ordinal)
```

```text
{"A", "B", "Z", "a", "b", "z"}
```

Comparing a null with text raises an error, though two nulls compare equal (0); non-text values such as numbers are still compared (2 sorts before 10).

```m
{Comparer.Ordinal(null, "a"), Comparer.Ordinal("a", null), Comparer.Ordinal(null, null), Comparer.Ordinal(2, 10)}
```

```text
{error: Expression.Error: We cannot apply operator < to types Null and Text. | Detail: [Operator = "<", Left = null, Right = "a"], error: Expression.Error: We cannot apply operator < to types Text and Null. | Detail: [Operator = "<", Left = "a", Right = null], 0, -1}
```
