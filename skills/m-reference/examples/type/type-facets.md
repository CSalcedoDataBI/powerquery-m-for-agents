<!-- lab: desktop 2.157.879.0 -->

# Type.Facets

These examples show the facets reported for a plain type, a nullable type, and the type of `null`.

```m
Type.Facets(type number)
```

```text
[NumericPrecisionBase = null, NumericPrecision = null, NumericScale = null, IsSigned = null, DateTimePrecision = null, MaxLength = null, IsVariableLength = null, NativeTypeName = null, NativeDefaultExpression = null, NativeExpression = null]
```

```m
Type.Facets(type nullable number)
```

```text
[NumericPrecisionBase = null, NumericPrecision = null, NumericScale = null, IsSigned = null, DateTimePrecision = null, MaxLength = null, IsVariableLength = null, NativeTypeName = null, NativeDefaultExpression = null, NativeExpression = null]
```

```m
Type.Facets(Value.Type(null))
```

```text
[NumericPrecisionBase = null, NumericPrecision = null, NumericScale = null, IsSigned = null, DateTimePrecision = null, MaxLength = null, IsVariableLength = null, NativeTypeName = null, NativeDefaultExpression = null, NativeExpression = null]
```
