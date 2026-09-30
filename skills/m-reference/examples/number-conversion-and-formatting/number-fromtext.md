<!-- lab: desktop 2.157.879.0 -->

# Number.FromText

Null text yields null, the optional culture changes how separators are read, and text without a valid number raises an error.

```m
Number.FromText(null)
```

```text
null
```

The culture argument is optional but decisive when a comma is involved.

```m
Number.FromText("1.234,5", "de-DE")
```

```text
1234.5
```

A string that does not hold a valid number fails instead of returning null.

```m
Number.FromText("12 apples")
```

```text
error: DataFormat.Error: We couldn't convert to Number. | Detail: "12 apples"
```
