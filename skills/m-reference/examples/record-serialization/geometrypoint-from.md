<!-- lab: desktop 2.157.879.0 -->

# GeometryPoint.From

Optional arguments are positional, so setting M without Z means passing null for Z.

```m
GeometryPoint.From(1, 2)
```

```text
[Kind = "POINT", X = 1, Y = 2]
```

```m
GeometryPoint.From(1, 2, 3, 4, 4326)
```

```text
[Kind = "POINT", X = 1, Y = 2, Z = 3, M = 4, SRID = 4326]
```

```m
GeometryPoint.From(1, 2, null, 4)
```

```text
[Kind = "POINT", X = 1, Y = 2, M = 4]
```
