<!-- lab: desktop 2.157.879.0 -->

# Percentage.From

These examples show what happens with `null`, text that has no percent symbol, and the optional `culture` argument.

A `null` input returns `null` rather than an error.

```m
Percentage.From(null)
```

```text
null
```

Without a percent sign the text is read as a plain number: nothing is divided by 100.

```m
Percentage.From("12.3")
```

```text
12.3
```

Culture matters when the text uses a comma as the decimal separator.

```m
Percentage.From("12,3%", "de-DE")
```

```text
0.123
```
