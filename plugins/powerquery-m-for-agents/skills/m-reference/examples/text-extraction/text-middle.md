<!-- lab: desktop 2.157.879.0 -->

# Text.Middle

Past the end it returns what is there, even nothing, instead of an error.

```m
{Text.Middle("Hello", 1, 3), Text.Middle("Hello", 3, 10), Text.Middle("Hello", 10, 2)}
```

```text
{"ell", "lo", ""}
```
