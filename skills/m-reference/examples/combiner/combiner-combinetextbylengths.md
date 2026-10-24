<!-- lab: desktop 2.159.883.0 -->

# Combiner.CombineTextByLengths

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
