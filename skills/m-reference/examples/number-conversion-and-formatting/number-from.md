<!-- lab: desktop 2.157.879.0 -->

# Number.From

Null is preserved and the optional culture argument changes how text is read.

```m
Number.From(null)
```

```text
null
```

Culture changes the meaning of separators, so the same text parses differently.

```m
Number.From("1.234,56", "de-DE")
```

```text
1234.56
```

Logical, time, and duration values convert as well.

```m
List.Transform({true, false, #time(6, 0, 0), #duration(1, 12, 0, 0)}, Number.From)
```

```text
{1, 0, 0.25, 1.5}
```
