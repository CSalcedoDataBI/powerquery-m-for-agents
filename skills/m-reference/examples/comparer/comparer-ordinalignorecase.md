<!-- lab: desktop 2.159.883.0 -->

# Comparer.OrdinalIgnoreCase

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
