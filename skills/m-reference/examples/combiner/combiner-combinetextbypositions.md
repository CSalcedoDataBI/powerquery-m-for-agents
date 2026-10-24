<!-- lab: desktop 2.159.883.0 -->

# Combiner.CombineTextByPositions

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
