<!-- lab: desktop 2.157.879.0 -->

# Splitter.SplitTextByRepeatedLengths

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
