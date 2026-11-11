<!-- lab: desktop 2.159.883.0 -->

# Executed examples: comparer

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Comparer.Equals

These examples show how the comparer you pass changes the result.

```m
[Ordinal = Comparer.Equals(Comparer.Ordinal, "apple", "APPLE"), IgnoreCase = Comparer.Equals(Comparer.OrdinalIgnoreCase, "apple", "APPLE")]
```

```text
[Ordinal = false, IgnoreCase = true]
```

Nulls, empty text and mixed types under the same comparer.

```m
[NullNull = Comparer.Equals(Comparer.Ordinal, null, null), NullEmpty = Comparer.Equals(Comparer.Ordinal, null, ""), IntDecimal = Comparer.Equals(Comparer.Ordinal, 1, 1.0), NumberText = Comparer.Equals(Comparer.Ordinal, 1, "1")]
```

```text
[NullNull = true, NullEmpty = false, IntDecimal = true, NumberText = false]
```

With ignore-case on, the culture still decides which letters match.

```m
[EnUS = Comparer.Equals(Comparer.FromCulture("en-US", true), "i", "I"), TrTR = Comparer.Equals(Comparer.FromCulture("tr-TR", true), "i", "I")]
```

```text
[EnUS = true, TrTR = false]
```

## Comparer.FromCulture

These examples show how the culture and the optional `ignoreCase` argument change the comparer's result.

```m
[
    Default = Comparer.FromCulture("en-US")("a", "A"),
    NullIgnoreCase = Comparer.FromCulture("en-US", null)("a", "A"),
    IgnoreCase = Comparer.FromCulture("en-US", true)("a", "A")
]
```

```text
[Default = -1, NullIgnoreCase = -1, IgnoreCase = 0]
```

Case-insensitive matching depends on the culture's casing rules. In Turkish, the uppercase form of `i` is `İ`, not `I`.

```m
{
    Comparer.FromCulture("en-US", true)("i", "I"),
    Comparer.FromCulture("tr-TR", true)("i", "I")
}
```

```text
{0, 1}
```

As a sort comparer, the culture orders strings differently from ordinal comparison.

```m
[
    Culture = List.Sort({"b", "B", "a", "A"}, Comparer.FromCulture("en-US")),
    Ordinal = List.Sort({"b", "B", "a", "A"}, Comparer.Ordinal)
]
```

```text
[Culture = {"a", "A", "b", "B"}, Ordinal = {"A", "B", "a", "b"}]
```

## Comparer.Ordinal

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

## Comparer.OrdinalIgnoreCase

These examples show what counts as a case difference, where the ordering differs from case-sensitive `Comparer.Ordinal`, and how nulls compare.

```m
[
    SameWord = Comparer.OrdinalIgnoreCase("Hello", "HELLO"),
    AvsB = Comparer.OrdinalIgnoreCase("a", "B"),
    AvsBCaseSensitive = Comparer.Ordinal("a", "B"),
    Accented = Comparer.OrdinalIgnoreCase("é", "É"),
    SharpS = Comparer.OrdinalIgnoreCase("straße", "STRASSE"),
    TrailingSpace = Comparer.OrdinalIgnoreCase("abc", "ABC "),
    NullVsText = Comparer.OrdinalIgnoreCase(null, "a"),
    NullVsNull = Comparer.OrdinalIgnoreCase(null, null)
]
```

```text
[SameWord = 0, AvsB = -1, AvsBCaseSensitive = 1, Accented = 0, SharpS = 1, TrailingSpace = -1, NullVsText = error: Expression.Error: We cannot apply operator < to types Null and Text. | Detail: [Operator = "<", Left = null, Right = "a"], NullVsNull = 0]
```

The same function can be passed as the optional comparer argument of other library functions.

```m
[
    Distinct = List.Distinct({"apple", "Apple", "APPLE", "banana"}, Comparer.OrdinalIgnoreCase),
    Contains = Text.Contains("Power Query", "query", Comparer.OrdinalIgnoreCase),
    ContainsDefault = Text.Contains("Power Query", "query"),
    Sorted = List.Sort({"b", "A", "c", "B", "a"}, Comparer.OrdinalIgnoreCase),
    SortedDefault = List.Sort({"b", "A", "c", "B", "a"})
]
```

```text
[Distinct = {"apple", "banana"}, Contains = true, ContainsDefault = false, Sorted = {"A", "a", "b", "B", "c"}, SortedDefault = {"A", "B", "a", "b", "c"}]
```

Values that are not text can also be passed.

```m
[
    Numbers = Comparer.OrdinalIgnoreCase(2, 10),
    NumberTexts = Comparer.OrdinalIgnoreCase("2", "10")
]
```

```text
[Numbers = -1, NumberTexts = 1]
```
