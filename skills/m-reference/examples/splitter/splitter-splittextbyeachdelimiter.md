<!-- lab: desktop 2.157.879.0 -->

# Splitter.SplitTextByEachDelimiter

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
