<!-- lab: desktop 2.157.879.0 -->

# Byte.From

Nulls pass through, and the default rounding of a fractional value is not the one you might expect.

```m
Byte.From(null)
```

```text
null
```

With no rounding mode, a fractional value rounds to the nearest even integer.

```m
Byte.From("4.5")
```

```text
4
```

Naming a rounding mode while leaving `culture` unset rounds the other way.

```m
Byte.From("4.5", null, RoundingMode.AwayFromZero)
```

```text
5
```
