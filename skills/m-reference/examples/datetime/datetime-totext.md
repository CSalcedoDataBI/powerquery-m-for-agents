<!-- lab: desktop 2.157.879.0 -->

# DateTime.ToText

These examples show how a null input, the legacy text `options` form, and a record that omits `Format` behave.

```m
DateTime.ToText(null)
```

```text
null
```

```m
DateTime.ToText(#datetime(2010, 12, 30, 2, 4, 50.36973), "dd MMM yyyy", "de-DE")
```

```text
"30 Dez 2010"
```

```m
DateTime.ToText(#datetime(2010, 12, 31, 13, 30, 25), [Format = null, Culture = "en-US"])
```

```text
"12/31/2010 1:30:25 PM"
```
