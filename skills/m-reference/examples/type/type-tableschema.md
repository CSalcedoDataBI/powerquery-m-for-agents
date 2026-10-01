<!-- lab: desktop 2.157.879.0 -->

# Type.TableSchema

The schema comes from the declared type alone, so null-friendly types and even a column-less type still describe a table.

```m
Type.TableSchema(type table [Name = text, Score = number])
```

```text
#table(type table [Name = text, Position = number, TypeName = text, Kind = text, IsNullable = logical, NumericPrecisionBase = nullable number, NumericPrecision = nullable number, NumericScale = nullable number, IsSigned = nullable logical, DateTimePrecision = nullable number, MaxLength = nullable number, IsVariableLength = nullable logical, NativeTypeName = nullable text, NativeDefaultExpression = nullable text, NativeExpression = nullable text, Description = nullable text, IsWritable = nullable logical, FieldCaption = nullable text], {{"Name", 0, "Text.Type", "text", false, null, null, null, null, null, null, null, null, null, null, null, null, null}, {"Score", 1, "Number.Type", "number", false, null, null, null, null, null, null, null, null, null, null, null, null, null}})
```

```m
Type.TableSchema(type table [Note = any, Amount = nullable number])
```

```text
#table(type table [Name = text, Position = number, TypeName = text, Kind = text, IsNullable = logical, NumericPrecisionBase = nullable number, NumericPrecision = nullable number, NumericScale = nullable number, IsSigned = nullable logical, DateTimePrecision = nullable number, MaxLength = nullable number, IsVariableLength = nullable logical, NativeTypeName = nullable text, NativeDefaultExpression = nullable text, NativeExpression = nullable text, Description = nullable text, IsWritable = nullable logical, FieldCaption = nullable text], {{"Note", 0, "Any.Type", "any", true, null, null, null, null, null, null, null, null, null, null, null, null, null}, {"Amount", 1, "Number.Type", "number", true, null, null, null, null, null, null, null, null, null, null, null, null, null}})
```

```m
Type.TableSchema(type table [])
```

```text
#table(type table [Name = text, Position = number, TypeName = text, Kind = text, IsNullable = logical, NumericPrecisionBase = nullable number, NumericPrecision = nullable number, NumericScale = nullable number, IsSigned = nullable logical, DateTimePrecision = nullable number, MaxLength = nullable number, IsVariableLength = nullable logical, NativeTypeName = nullable text, NativeDefaultExpression = nullable text, NativeExpression = nullable text, Description = nullable text, IsWritable = nullable logical, FieldCaption = nullable text], {})
```
