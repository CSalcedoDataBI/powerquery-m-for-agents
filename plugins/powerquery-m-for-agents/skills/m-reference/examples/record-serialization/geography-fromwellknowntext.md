<!-- lab: desktop 2.157.879.0 -->

# Geography.FromWellKnownText

Null input returns null, and the parser is case-insensitive about WKT keywords and forgiving of extra whitespace.

A null value returns null instead of raising an error.

```m
Geography.FromWellKnownText(null)
```

```text
null
```

Keyword case and surrounding spaces do not matter.

```m
Geography.FromWellKnownText("  point ( -122.35 47.68 ) ")
```

```text
[Kind = "POINT", Longitude = -122.35, Latitude = 47.68]
```

Multi-vertex geometries parse as well, not just points.

```m
Geography.FromWellKnownText("LINESTRING (0 0, 1 1, 2 2)")
```

```text
[Kind = "LINESTRING", Points = {[Kind = "POINT", Longitude = 0, Latitude = 0], [Kind = "POINT", Longitude = 1, Latitude = 1], [Kind = "POINT", Longitude = 2, Latitude = 2]}]
```
