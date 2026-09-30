<!-- lab: desktop 2.157.879.0 -->

# Number.ToText

The examples show null handling, culture-sensitive separators, and standard format strings.

```m
Number.ToText(null)
```

```text
null
```

```m
Number.ToText(1234.5678, "N2", "de-DE")
```

```text
"1.234,57"
```

```m
[
    default = Number.ToText(4),
    exponential = Number.ToText(4, "e"),
    percent = Number.ToText(-0.1234, "P1", "en-US")
]
```

```text
[default = "4", exponential = "4.000000e+000", percent = "-12.3%"]
```
