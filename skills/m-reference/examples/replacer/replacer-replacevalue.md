<!-- lab: desktop 2.159.883.0 -->

# Replacer.ReplaceValue

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
