<!-- lab: desktop 2.157.879.0 -->

# Splitter.SplitByNothing

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
