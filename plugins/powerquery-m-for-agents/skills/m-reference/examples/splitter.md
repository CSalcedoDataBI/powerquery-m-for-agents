<!-- lab: desktop 2.157.879.0 -->

# Executed examples: splitter

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Splitter.SplitByNothing

The splitter leaves its input whole and returns a one-item list, whatever the input is.

A null input is wrapped as an item rather than giving an empty list.

```m
Splitter.SplitByNothing()(null)
```

```text
{null}
```

A list input is wrapped whole, so the result is a list holding one list.

```m
Splitter.SplitByNothing()({1, 2, 3})
```

```text
{{1, 2, 3}}
```

The splitter never looks for delimiters, so text with commas still comes back as one item.

```m
List.Count(Splitter.SplitByNothing()("a,b,c"))
```

```text
1
```

## Splitter.SplitTextByAnyDelimiter

A null quote style acts like `QuoteStyle.Csv`: the quoted comma does not split. The last block shows `startAtEnd` with an unmatched quote, where the result does not follow a left-to-right reading.

```m
Splitter.SplitTextByAnyDelimiter({","}, null, null)("""a,b"",c")
```

```text
{"a,b", "c"}
```

```m
Splitter.SplitTextByAnyDelimiter({","}, QuoteStyle.Csv)("""a,b"",c")
```

```text
{"a,b", "c"}
```

```m
Splitter.SplitTextByAnyDelimiter({",", ";"}, QuoteStyle.Csv, true)("a,""b;c,d")
```

```text
{"a,b", "c", "d"}
```

## Splitter.SplitTextByCharacterTransition

These examples show which character transitions cause a split, using both list and predicate forms.

A split is made before each `after` character that directly follows a `before` character.

```m
Splitter.SplitTextByCharacterTransition({"A".."Z"}, {"a".."z"})("XMLHttpRequest")
```

```text
{"XMLH", "ttpR", "equest"}
```

Either argument can be a predicate function instead of a character list, and the two arguments are chosen independently.

```m
Splitter.SplitTextByCharacterTransition({"0".."9"}, each not List.Contains({"0".."9"}, _))("a1b2c")
```

```text
{"a1", "b2", "c"}
```

A null text gives an empty list, not null.

```m
Splitter.SplitTextByCharacterTransition({"a"}, {"b"})(null)
```

```text
{}
```

## Splitter.SplitTextByDelimiter

Quotes group text even without `QuoteStyle.Csv`, and a null input gives an empty list.

```m
Splitter.SplitTextByDelimiter(",")("a,""b,c"",d")
```

```text
{"a", "b,c", "d"}
```

```m
Splitter.SplitTextByDelimiter(",", QuoteStyle.Csv)("a,""b,c"",d")
```

```text
{"a", "b,c", "d"}
```

```m
Splitter.SplitTextByDelimiter(",")(null)
```

```text
{}
```

## Splitter.SplitTextByEachDelimiter

Each delimiter is used only once, in the order given, never at every occurrence.

```m
Splitter.SplitTextByEachDelimiter({",", ";"})("a,b;c,d;e")
```

```text
{"a", "b", "c,d;e"}
```

A single delimiter therefore splits only at its first occurrence.

```m
Splitter.SplitTextByEachDelimiter({","})("a,b,c")
```

```text
{"a", "b,c"}
```

Null is accepted for the optional quote style, and `startAtEnd` picks occurrences from the end.

```m
Splitter.SplitTextByEachDelimiter({",", ";"}, null, true)("a,b;c,d;e")
```

```text
{"a,b", "c", "d;e"}
```

## Splitter.SplitTextByLengths

The examples show the optional `startAtEnd` argument, how `null` is treated, and what happens to text beyond the given lengths.

```m
Splitter.SplitTextByLengths({2, 3})("AB12345")
```

```text
{"AB", "123"}
```

```m
Splitter.SplitTextByLengths({2, 3}, true)("AB12345")
```

```text
{"123", "45"}
```

```m
Splitter.SplitTextByLengths({2, 3}, null)("AB123")
```

```text
{"AB", "123"}
```

## Splitter.SplitTextByPositions

A position can repeat, which gives an empty item.

```m
Splitter.SplitTextByPositions({0, 3, 3, 4})("ABC|12345")
```

```text
{"ABC", "", "|", "12345"}
```

With `startAtEnd` set to true, positions count from the end of the text.

```m
let
    startAtEnd = true
in
    Splitter.SplitTextByPositions({0, 5}, startAtEnd)("Redmond98052")
```

```text
{"Redmond", "98052"}
```

The optional argument also accepts null.

```m
let
    startAtEnd = null
in
    Splitter.SplitTextByPositions({0, 3, 4}, startAtEnd)("ABC|12345")
```

```text
{"ABC", "|", "12345"}
```

## Splitter.SplitTextByRanges

These examples show null lengths, overlapping ranges, and the optional startAtEnd flag.

```m
Splitter.SplitTextByRanges({{0, 5}, {5, null}}, false)("98052Redmond")
```

```text
{"98052", "Redmond"}
```

Ranges can overlap and need not cover the whole input.

```m
Splitter.SplitTextByRanges({{0, 4}, {2, 10}})("codelimiter")
```

```text
{"code", "delimiter"}
```

With startAtEnd true, offsets are measured back from the end of the input.

```m
Splitter.SplitTextByRanges({{0, 5}, {6, 2}}, true)("RedmondWA?98052")
```

```text
{"WA", "98052"}
```

## Splitter.SplitTextByRepeatedLengths

These examples show how the optional `startAtEnd` argument handles null, where the short piece lands when splitting from the end, and how an exact-multiple input is split.

```m
Splitter.SplitTextByRepeatedLengths(3, null)("12345678")
```

```text
{"123", "456", "78"}
```

```m
Splitter.SplitTextByRepeatedLengths(3, true)("12345678")
```

```text
{"12", "345", "678"}
```

```m
Splitter.SplitTextByRepeatedLengths(3)("123456")
```

```text
{"123", "456"}
```

## Splitter.SplitTextByWhitespace

These examples show how quote characters, the optional quote style, and a null quote-style argument change the split.

Without a quote style, quotes still group: the quoted run keeps its double space as one item.

```m
Splitter.SplitTextByWhitespace()("a ""b  c"" d")
```

```text
{"a", "b  c", "d"}
```

Passing `QuoteStyle.Csv` keeps a quoted section, including its internal whitespace, together as one item.

```m
Splitter.SplitTextByWhitespace(QuoteStyle.Csv)("a ""b c"" d")
```

```text
{"a", "b c", "d"}
```

A null quote style behaves like the default, a tab separates items too, and the quotes around `c` are removed.

```m
Splitter.SplitTextByWhitespace(null)("a#(tab)b ""c""")
```

```text
{"a", "b", "c"}
```
