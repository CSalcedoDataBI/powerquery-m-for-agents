<!-- lab: desktop 2.157.879.0 -->

# Geometry.ToWellKnownText

These examples show how a geometry record serializes to Well-Known Text, including the effect of the optional `omitSRID` argument and how a null input is handled.

```m
Geometry.ToWellKnownText(GeometryPoint.From(30, 10, null, null, 4326))
```

```text
"SRID=4326;POINT(30 10)"
```

```m
Geometry.ToWellKnownText(GeometryPoint.From(30, 10, null, null, 4326), true)
```

```text
"POINT(30 10)"
```

```m
Geometry.ToWellKnownText(null)
```

```text
null
```
