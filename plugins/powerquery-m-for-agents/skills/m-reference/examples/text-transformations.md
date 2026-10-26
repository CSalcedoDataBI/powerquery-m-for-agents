<!-- lab: desktop 2.157.879.0 -->

# Executed examples: text-transformations

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Text.AfterDelimiter

After the first delimiter, and after the first one counted from the end.

```m
{Text.AfterDelimiter("111-222-333", "-"), Text.AfterDelimiter("111-222-333", "-", {0, RelativePosition.FromEnd})}
```

```text
{"222-333", "333"}
```

## Text.BeforeDelimiter

Before the second delimiter (index 1).

```m
Text.BeforeDelimiter("111-222-333", "-", 1)
```

```text
"111-222"
```

## Text.BetweenDelimiters

Between the second pair of delimiters.

```m
Text.BetweenDelimiters("a (b) c (d)", "(", ")", 1)
```

```text
"d"
```

## Text.Clean

Control characters are removed, not replaced by spaces.

```m
Text.Clean("a#(lf)b#(tab)c")
```

```text
"abc"
```

## Text.Combine

A null item is skipped, with no separator left for it.

```m
Text.Combine({"a", null, "b"}, ", ")
```

```text
"a, b"
```

## Text.Lower

Lower case, accented letters included.

```m
Text.Lower("ÀBC")
```

```text
"àbc"
```

## Text.PadEnd

Pad on the right with a chosen character.

```m
Text.PadEnd("7", 3, ".")
```

```text
"7.."
```

## Text.PadStart

Leading zeros.

```m
{Text.PadStart("7", 3, "0"), Text.PadStart("1234", 3, "0")}
```

```text
{"007", "1234"}
```

## Text.Proper

Every word is capitalised; the rest is lowered.

```m
Text.Proper("mcDONALD o'brien")
```

```text
"Mcdonald O'Brien"
```

## Text.Repeat

Repeat a text.

```m
Text.Repeat("ab", 3)
```

```text
"ababab"
```

## Text.Reverse

Reverse the characters.

```m
Text.Reverse("abc")
```

```text
"cba"
```

## Text.Split

Empty pieces are kept.

```m
Text.Split("a,,b", ",")
```

```text
{"a", "", "b"}
```

## Text.SplitAny

Split on any of several characters.

```m
Text.SplitAny("a,b;c", ",;")
```

```text
{"a", "b", "c"}
```

## Text.Trim

Spaces by default, or the characters given.

```m
{Text.Trim("  a  "), Text.Trim("--a--", "-")}
```

```text
{"a", "a"}
```

## Text.TrimEnd

Trailing characters only.

```m
Text.TrimEnd("a000", "0")
```

```text
"a"
```

## Text.TrimStart

Leading characters only.

```m
Text.TrimStart("000123", "0")
```

```text
"123"
```

## Text.Upper

The German sharp s has no single upper-case letter: it is kept as it is.

```m
{Text.Upper("abc"), Text.Upper("straße")}
```

```text
{"ABC", "STRAßE"}
```
