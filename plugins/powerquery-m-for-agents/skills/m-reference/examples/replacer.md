<!-- lab: desktop 2.159.883.0 -->

# Executed examples: replacer

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Replacer.ReplaceText

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

## Replacer.ReplaceValue

The whole value must equal `old` for a replacement; partial text, different case or a different type leave the value unchanged.

```m
{
    Replacer.ReplaceValue("abc", "abc", "x"),
    Replacer.ReplaceValue("abcd", "abc", "x"),
    Replacer.ReplaceValue("ABC", "abc", "x")
}
```

```text
{"x", "abcd", "ABC"}
```

```m
{
    Replacer.ReplaceValue(null, null, 0),
    Replacer.ReplaceValue(5, null, 0),
    Replacer.ReplaceValue(null, 5, 0)
}
```

```text
{0, 5, null}
```

```m
{
    Replacer.ReplaceValue(1, 1.0, "one"),
    Replacer.ReplaceValue("1", 1, "one"),
    Table.ReplaceValue(#table({"A"}, {{"abc"}, {"abcd"}, {null}}), null, "none", Replacer.ReplaceValue, {"A"})
}
```

```text
{"one", "1", #table(type table [A = any], {{"abc"}, {"abcd"}, {"none"}})}
```
