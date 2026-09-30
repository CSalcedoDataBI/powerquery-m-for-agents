<!-- lab: desktop 2.157.879.0 -->

# Double.From

Nulls pass through, the optional culture changes how text is read, and a number past the Double range becomes infinity, not an error.

```m
Double.From(null)
```

```text
null
```

```m
Double.From("1,5", "fr-FR")
```

```text
1.5
```

```m
Double.From(Number.Power(2, 1024))
```

```text
#infinity
```
