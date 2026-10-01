<!-- lab: desktop 2.157.879.0 -->

# Geography.ToWellKnownText

A null input returns null, and `omitSRID` decides whether a point's SRID is written as an `SRID=` prefix.

```m
Geography.ToWellKnownText(null)
```

```text
null
```

```m
Geography.ToWellKnownText(GeographyPoint.From(-122.349, 47.651, null, null, 4258))
```

```text
"SRID=4258;POINT(-122.349 47.651)"
```

```m
Geography.ToWellKnownText(GeographyPoint.From(-122.349, 47.651, null, null, 4258), true)
```

```text
"POINT(-122.349 47.651)"
```
