<!-- lab: desktop 2.157.879.0 -->

# Single.From

These examples show how `Single.From` handles `null`, the optional `culture` argument, and values outside the Single range.

```m
Single.From(null)
```

```text
null
```

```m
Single.From("1,5", "fr-FR")
```

```text
1.5
```

```m
Single.From(1E39)
```

```text
#infinity
```
