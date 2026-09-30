<!-- lab: desktop 2.157.879.0 -->

# Number.From

Text, logicals, a date and a duration.

```m
{Number.From("10"), Number.From(true), Number.From(#date(1899, 12, 31)), Number.From(#duration(1, 12, 0, 0))}
```

```text
{10, 1, 1, 1.5}
```

The culture decides how text is read.

```m
{Number.From("1,5", "es-ES"), Number.From("1,5", "en-US")}
```

```text
{1.5, 15}
```
