<!-- lab: desktop 2.157.879.0 -->

# List.ReplaceValue

The replacer decides: part of a text, or the whole value.

```m
{List.ReplaceValue({"ab", "b"}, "b", "z", Replacer.ReplaceText), List.ReplaceValue({"ab", "b"}, "b", "z", Replacer.ReplaceValue)}
```

```text
{{"az", "z"}, {"ab", "z"}}
```
