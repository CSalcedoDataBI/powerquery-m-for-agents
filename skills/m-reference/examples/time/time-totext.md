<!-- lab: desktop 2.159.883.0 -->

# Time.ToText

Format strings, culture, and null input.

```m
Time.ToText(#time(14, 5, 9), [Format = "hh:mm tt", Culture = "en-US"])
```

```text
"02:05 PM"
```

```m
Time.ToText(#time(14, 5, 9), [Format = "HH:mm:ss", Culture = "de-DE"])
```

```text
"14:05:09"
```

```m
Time.ToText(null)
```

```text
null
```
