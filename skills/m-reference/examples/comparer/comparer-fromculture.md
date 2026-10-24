<!-- lab: desktop 2.159.883.0 -->

# Comparer.FromCulture

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
