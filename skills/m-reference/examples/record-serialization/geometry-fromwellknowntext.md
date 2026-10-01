<!-- lab: desktop 2.157.879.0 -->

# Geometry.FromWellKnownText

The examples show how a null input and geometries with no coordinates or nested members are handled.

```m
Geometry.FromWellKnownText(null)
```

```text
null
```

```m
Geometry.FromWellKnownText("POINT EMPTY")
```

```text
[Kind = "POINT", X = #nan, Y = #nan]
```

```m
Geometry.FromWellKnownText("GEOMETRYCOLLECTION (POINT (10 10), LINESTRING (15 15, 20 20))")
```

```text
[Kind = "GEOMETRYCOLLECTION", Components = {[Kind = "POINT", X = 10, Y = 10], [Kind = "LINESTRING", Points = {[Kind = "POINT", X = 15, Y = 15], [Kind = "POINT", X = 20, Y = 20]}]}]
```
