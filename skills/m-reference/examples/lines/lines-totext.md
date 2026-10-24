<!-- lab: desktop 2.159.883.0 -->

# Lines.ToText

The separator follows every line, including the last one.

```m
Lines.ToText({"a", "b", "c"})
```

```text
"a#(cr)#(lf)b#(cr)#(lf)c#(cr)#(lf)"
```

A custom separator also trails the last line.

```m
Lines.ToText({"a", "b", "c"}, ", ")
```

```text
"a, b, c, "
```

A null separator, an empty list and a list holding one empty string.

```m
[NullSeparator = Lines.ToText({"a", "b"}, null), EmptyList = Lines.ToText({}), OneEmptyLine = Lines.ToText({""}, "|")]
```

```text
[NullSeparator = "a#(cr)#(lf)b#(cr)#(lf)", EmptyList = "", OneEmptyLine = "|"]
```
