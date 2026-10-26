<!-- lab: desktop 2.157.879.0 -->

# Type.ReplaceFacets

Facets describe a primitive type more precisely, such as the maximum length of a text.

```m
Type.Facets(Type.ReplaceFacets(type text, [MaxLength = 10, IsVariableLength = false]))
```

```text
[NumericPrecisionBase = null, NumericPrecision = null, NumericScale = null, IsSigned = null, DateTimePrecision = null, MaxLength = 10, IsVariableLength = false, NativeTypeName = null, NativeDefaultExpression = null, NativeExpression = null]
```

Replacing facets replaces the whole set: a facet set before and not given again is cleared.

```m
Type.Facets(Type.ReplaceFacets(Type.ReplaceFacets(type text, [MaxLength = 10]), [NativeTypeName = "nvarchar"]))
```

```text
[NumericPrecisionBase = null, NumericPrecision = null, NumericScale = null, IsSigned = null, DateTimePrecision = null, MaxLength = null, IsVariableLength = null, NativeTypeName = "nvarchar", NativeDefaultExpression = null, NativeExpression = null]
```

Only the facet names the engine knows are accepted.

```m
Type.ReplaceFacets(type text, [Color = 1])
```

```text
error: Expression.Error: The facet 'Color' is not supported. | Detail: [Color = 1]
```
