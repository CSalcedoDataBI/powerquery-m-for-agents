<!-- lab: desktop 2.157.879.0 -->

# Number.ToText

Format strings.

```m
{Number.ToText(1234.5), Number.ToText(1234.5, "N2"), Number.ToText(0.256, "P1"), Number.ToText(255, "X")}
```

```text
{"1234.5", "1,234.50", "25.6%", "FF"}
```

The culture changes the separators.

```m
{Number.ToText(1234.5, "N2", "en-US"), Number.ToText(1234.5, "N2", "de-DE")}
```

```text
{"1,234.50", "1.234,50"}
```
