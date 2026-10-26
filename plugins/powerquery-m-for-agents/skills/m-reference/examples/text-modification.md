<!-- lab: desktop 2.157.879.0 -->

# Executed examples: text-modification

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Text.Insert

Insert at a zero-based offset.

```m
Text.Insert("ABD", 2, "C")
```

```text
"ABCD"
```

## Text.Remove

Remove every listed character.

```m
Text.Remove("a-b_c", {"-", "_"})
```

```text
"abc"
```

## Text.RemoveRange

Remove a count of characters from an offset.

```m
Text.RemoveRange("ABCDEF", 2, 2)
```

```text
"ABEF"
```

## Text.Replace

Every occurrence is replaced.

```m
Text.Replace("a.b.c", ".", "-")
```

```text
"a-b-c"
```

## Text.ReplaceRange

Replace a range with a text of another length.

```m
Text.ReplaceRange("ABCDEF", 2, 2, "xyz")
```

```text
"ABxyzEF"
```

## Text.Select

Keep only digits.

```m
Text.Select("a1b2c3", {"0".."9"})
```

```text
"123"
```
