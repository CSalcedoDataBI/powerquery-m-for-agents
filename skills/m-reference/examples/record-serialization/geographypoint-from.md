<!-- lab: desktop 2.157.879.0 -->

# GeographyPoint.From

The examples show omitted optional arguments, a null placeholder for elevation, and a custom SRID.

```m
GeographyPoint.From(-122.3321, 47.6062)
```

```text
[Kind = "POINT", Longitude = -122.3321, Latitude = 47.6062]
```

A null elevation is allowed, so a measure can be supplied without a Z value.

```m
GeographyPoint.From(-122.3321, 47.6062, null, 5000)
```

```text
[Kind = "POINT", Longitude = -122.3321, Latitude = 47.6062, M = 5000]
```

Because the optional arguments are positional, a custom SRID must follow values (or nulls) for both Z and M.

```m
GeographyPoint.From(-122.3321, 47.6062, 35, null, 4258)
```

```text
[Kind = "POINT", Longitude = -122.3321, Latitude = 47.6062, Z = 35, SRID = 4258]
```
