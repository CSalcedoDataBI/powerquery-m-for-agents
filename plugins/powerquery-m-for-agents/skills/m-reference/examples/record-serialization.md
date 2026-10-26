<!-- lab: desktop 2.157.879.0 -->

# Executed examples: record-serialization

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Geography.FromWellKnownText

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

## Geography.ToWellKnownText

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

## GeographyPoint.From

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

## Geometry.FromWellKnownText

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

## Geometry.ToWellKnownText

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

## GeometryPoint.From

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

## Record.FromList

Nulls are ordinary values, a record type supplies only field names and order, and duplicate field names are rejected.

```m
Record.FromList({null, "Bob"}, {"CustomerID", "Name"})
```

```text
[CustomerID = null, Name = "Bob"]
```

A record type does not convert the list values to the declared types.

```m
Record.FromList({"123-4567", 1}, type [Phone = number, CustomerID = text])
```

```text
[Phone = "123-4567", CustomerID = 1]
```

Duplicate field names are an error even when the values are valid.

```m
Record.FromList({1, 2}, {"ID", "ID"})
```

```text
error: Expression.Error: The field 'ID' already exists in the record. | Detail: [Name = "ID", Value = null]
```

## Record.FromTable

A null value is kept as the field's value, an empty table gives an empty record, and duplicate field names raise an error.

```m
Record.FromTable(Table.FromRecords({[Name = "CustomerID", Value = 1], [Name = "Phone", Value = null]}))
```

```text
[CustomerID = 1, Phone = null]
```

```m
Record.FromTable(#table({"Name", "Value"}, {}))
```

```text
[]
```

```m
Record.FromTable(Table.FromRecords({[Name = "ID", Value = 1], [Name = "ID", Value = 2]}))
```

```text
error: Expression.Error: The field 'ID' already exists in the record. | Detail: [Name = "ID", Value = null]
```

## Record.ToList

Collecting a record's field values keeps nulls, follows declaration order, and handles the empty record.

Null field values are kept as items, not dropped.

```m
Record.ToList([A = null, B = 2, C = null])
```

```text
{null, 2, null}
```

The values come out in the order the fields are declared, not in name order.

```m
Record.ToList([C = 3, A = 1])
```

```text
{3, 1}
```

An empty record produces an empty list.

```m
Record.ToList([])
```

```text
{}
```

## Record.ToTable

Field order follows the record's definition order, and null values are kept.

```m
Record.ToTable([B = null, A = 1])
```

```text
#table(type table [Name = text, Value = any], {{"B", null}, {"A", 1}})
```

An empty record yields the `Name` and `Value` columns with no rows.

```m
Record.ToTable([])
```

```text
#table(type table [Name = text, Value = any], {})
```

A nested record stays a single record value; it is not flattened into extra rows.

```m
Record.ToTable([A = [X = 1], B = 2])
```

```text
#table(type table [Name = text, Value = any], {{"A", [X = 1]}, {"B", 2}})
```
