<!-- lab: desktop 2.157.879.0 -->

# Text.AfterDelimiter

After the first delimiter, and after the first one counted from the end.

```m
{Text.AfterDelimiter("111-222-333", "-"), Text.AfterDelimiter("111-222-333", "-", {0, RelativePosition.FromEnd})}
```

```text
{"222-333", "333"}
```
