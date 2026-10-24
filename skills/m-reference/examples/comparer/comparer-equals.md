<!-- lab: desktop 2.159.883.0 -->

# Comparer.Equals

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
