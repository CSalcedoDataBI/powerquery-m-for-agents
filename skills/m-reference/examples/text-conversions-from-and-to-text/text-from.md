<!-- lab: desktop 2.157.879.0 -->

# Text.From

The culture decides the decimal separator.

```m
{Text.From(1234.5, "en-US"), Text.From(1234.5, "es-ES"), Text.From(null)}
```

```text
{"1234.5", "1234,5", null}
```
