<!-- lab: desktop 2.157.879.0 -->

# Int64.From

Halves round to even unless a mode says otherwise.

```m
{Int64.From(0.5), Int64.From(1.5), Int64.From(0.5, null, RoundingMode.Up)}
```

```text
{0, 2, 1}
```

Text in another culture, and null.

```m
{Int64.From("1.000", "de-DE"), Int64.From(null)}
```

```text
{1000, null}
```
