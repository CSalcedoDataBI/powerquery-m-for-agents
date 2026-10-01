<!-- lab: desktop 2.157.879.0 -->

# Splitter.SplitTextByLengths

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
