<!-- lab: desktop 2.159.883.0 -->

# Replacer.ReplaceText

These examples show that matching is case-sensitive, that every occurrence is replaced, how overlapping matches behave, and what happens with null text.

```m
[
    AllOccurrences = Replacer.ReplaceText("banana", "an", "_"),
    CaseSensitive = Replacer.ReplaceText("Banana", "b", "X"),
    Overlapping = Replacer.ReplaceText("aaaa", "aa", "b"),
    EmptyNew = Replacer.ReplaceText("a-b-c", "-", "")
]
```

```text
[AllOccurrences = "b__a", CaseSensitive = "Banana", Overlapping = "bb", EmptyNew = "abc"]
```

When the text is null, no replacement is made.

```m
Replacer.ReplaceText(null, "a", "b")
```

```text
null
```

Used in Table.ReplaceValue, it replaces part of a cell and skips null cells.

```m
Table.ReplaceValue(#table({"A"}, {{"red apple"}, {null}, {"Apple pie"}}), "apple", "pear", Replacer.ReplaceText, {"A"})
```

```text
#table(type table [A = nullable text], {{"red pear"}, {null}, {"Apple pie"}})
```
