<!-- lab: desktop 2.157.879.0 -->

# Splitter.SplitTextByRanges

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
