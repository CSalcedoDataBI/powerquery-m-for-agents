<!-- lab: desktop 2.157.879.0 -->

# List.TransformMany

Every item paired with every item of its collection.

```m
List.TransformMany({1, 2}, each {"a", "b"}, (x, y) => Text.From(x) & y)
```

```text
{"1a", "1b", "2a", "2b"}
```
