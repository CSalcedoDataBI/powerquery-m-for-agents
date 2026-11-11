<!-- lab: desktop 2.159.883.0 -->

# Executed examples: combiner

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Combiner.CombineTextByDelimiter

The function returns a combiner, which is applied to a list to show how nulls, delimiters inside values and quoteStyle change the joined text.

```m
Combiner.CombineTextByDelimiter(",")({"a", null, "c"})
```

```text
"a,,c"
```

Without quoteStyle, a value that contains the delimiter or a quote character may be quoted.

```m
Combiner.CombineTextByDelimiter(",")({"a,b", "say ""hi""", "c"})
```

```text
"""a,b"",""say """"hi"""""",c"
```

With QuoteStyle.None, the same values are joined as they are.

```m
Combiner.CombineTextByDelimiter(",", QuoteStyle.None)({"a,b", "say ""hi""", "c"})
```

```text
"a,b,say ""hi"",c"
```

## Combiner.CombineTextByEachDelimiter

Each delimiter is used once, in order, between consecutive items, and the examples show null items, running out of delimiters, and quoting.

```m
Combiner.CombineTextByEachDelimiter({"=", "+"})({"a", null, "c"})
```

```text
"a=+c"
```

With more items than delimiters, the items left over after the last delimiter show how the combiner handles the gaps it has no delimiter for.

```m
Combiner.CombineTextByEachDelimiter({"-"})({"a", "b", "c", "d"})
```

```text
"a-bcd"
```

With QuoteStyle.Csv, items that contain a delimiter or a quote character may be wrapped in quotes.

```m
Combiner.CombineTextByEachDelimiter({",", ";"}, QuoteStyle.Csv)({"x,y", "say ""hi""", "z;w"})
```

```text
"""x,y"",""say """"hi"""""";z;w"
```

## Combiner.CombineTextByLengths

The returned function places each piece into a fixed-width slot. These examples cover short pieces, long pieces, nulls and the optional template.

```m
Combiner.CombineTextByLengths({1, 2, 3})({"a", "bc", "def"})
```

```text
"abcdef"
```

A piece shorter than its length, a piece longer than its length, and a null piece.

```m
Combiner.CombineTextByLengths({3, 2, 3})({"a", "toolong", null})
```

```text
"a  to"
```

With a template longer than the slots, the pieces are written over the template's characters.

```m
Combiner.CombineTextByLengths({1, 2}, "**********")({"a", "b"})
```

```text
"ab********"
```

## Combiner.CombineTextByPositions

These examples show padding between positions, a custom template, text longer than its slot, and null items.

```m
Combiner.CombineTextByPositions({0, 5, 10})({"a", "b", "c"})
```

```text
"a    b    c"
```

A template supplies the characters between the placed texts, replacing the default spaces.

```m
Combiner.CombineTextByPositions({0, 5, 10}, "............")({"a", "b", "c"})
```

```text
"a....b....c."
```

Text longer than its slot meets the next position, and a null item leaves its slot empty.

```m
Combiner.CombineTextByPositions({0, 3, 6})({"abcdef", null, "xyz"})
```

```text
"abc   xyz"
```

## Combiner.CombineTextByRanges

These examples show truncation, gap filling, templates, null items and overlapping ranges.

```m
Combiner.CombineTextByRanges({{0, 3}, {5, 2}})({"abcdef", "xyz"})
```

```text
"abc  xy"
```

```m
Combiner.CombineTextByRanges({{0, 2}, {4, 2}}, "########")({"a", null})
```

```text
"a#######"
```

```m
Combiner.CombineTextByRanges({{0, 4}, {2, 3}}, "..........")({"AAAA", "BBB"})
```

```text
"AABBB....."
```
