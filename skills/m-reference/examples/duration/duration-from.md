<!-- lab: desktop 2.157.879.0 -->

# Duration.From

These examples show how a number, a text value, and a null each become a duration.

```m
Duration.From(2.525)
```

```text
#duration(2, 12, 36, 0)
```

Text uses the elapsed-time form `d.hh:mm:ss`, not a plain number.

```m
Duration.From("2.05:55:20.34567")
```

```text
#duration(2, 5, 55, 20.34567)
```

A null passes through instead of raising an error.

```m
Duration.From(null)
```

```text
null
```
