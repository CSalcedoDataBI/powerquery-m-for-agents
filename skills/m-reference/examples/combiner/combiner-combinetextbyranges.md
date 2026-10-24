<!-- lab: desktop 2.159.883.0 -->

# Combiner.CombineTextByRanges

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
