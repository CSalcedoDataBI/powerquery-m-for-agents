<!-- lab: desktop 2.157.879.0 -->

# Executed examples: type

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Function.IsDataSource

Anonymous and library functions are not data sources, and null is rejected.

```m
Function.IsDataSource((x, optional y) => x)
```

```text
false
```

```m
Function.IsDataSource(Text.Upper)
```

```text
false
```

```m
Function.IsDataSource(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Function. | Detail: [Value = null, Type = error: Expression.Error: Function.Type is abstract and has no defined parameters.]
```

## Type.AddTableKey

Adding a key returns a table type, and `Type.TableKeys` reads the key back.

```m
Type.TableKeys(Type.AddTableKey(type table [Id = number, Name = text], {"Id"}, true))
```

```text
{[Columns = {"Id"}, Primary = true]}
```

```m
Type.TableKeys(Type.AddTableKey(type table [Id = number, Name = text], {"Id"}, false))
```

```text
{[Columns = {"Id"}, Primary = false]}
```

```m
Type.TableKeys(Type.AddTableKey(type table [Region = text, Store = text, Sales = number], {"Region", "Store"}, true))
```

```text
{[Columns = {"Region", "Store"}, Primary = true]}
```

## Type.ClosedRecord

Closing an open record type drops the `...` marker while keeping each field's type, its `optional` marker and its `nullable` facet.

```m
Type.ClosedRecord(type [A = number, optional B = text, ...])
```

```text
type [A = number, optional B = text]
```

A nullability facet on a field type survives closing.

```m
Type.ClosedRecord(type [A = nullable number, ...])
```

```text
type [A = nullable number]
```

An already-closed record type is returned unchanged, so closing twice is the same as closing once.

```m
Type.ClosedRecord(Type.ClosedRecord(type [A = number, ...]))
```

```text
type [A = number]
```

## Type.Facets

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

## Type.ForFunction

The examples show how `min` marks trailing parameters optional and how a nullable parameter type differs from an optional one.

```m
Type.ForFunction([ReturnType = type number, Parameters = [X = type number, Y = type number]], 1)
```

```text
type function (X as number, optional Y as nullable number) as number
```

```m
Type.ForFunction([ReturnType = type nullable number, Parameters = [X = type nullable number]], 1)
```

```text
type function (X as nullable number) as nullable number
```

```m
Type.ForFunction([ReturnType = type logical, Parameters = [X = type logical]], 0)
```

```text
type function (optional X as nullable logical) as logical
```

## Type.ForRecord

`Value.Is` against a record type built here checks only that the value is a record: field types,
nullability and openness are not checked. All four are `true`, the last one with a number in a
text field.

```m
Value.Is([Name = null], Type.ForRecord([Name = [Type = type text, Optional = true]], false))
```

```text
true
```

```m
Value.Is([Name = null], Type.ForRecord([Name = [Type = type nullable text, Optional = false]], false))
```

```text
true
```

```m
Value.Is([Name = "x", Age = 1], Type.ForRecord([Name = [Type = type text, Optional = false]], true))
```

```text
true
```

```m
Value.Is([Name = 1], Type.ForRecord([Name = [Type = type text, Optional = false]], false))
```

```text
true
```

## Type.FunctionParameters

These examples show how a function's parameters come back as a record of `type` values, including optional and `any` parameters.

```m
Type.FunctionParameters(type function (x as any, y as text) as any)
```

```text
[x = type any, y = type text]
```

An optional parameter is listed like a required one, with its type made nullable.

```m
Type.FunctionParameters(type function (start as number, optional end as number) as any)
```

```text
[start = type number, end = type nullable number]
```

A function that takes no parameters yields an empty record.

```m
Type.FunctionParameters(type function () as any)
```

```text
[]
```

## Type.FunctionRequiredParameters

These examples show that only parameters not declared `optional` are counted.

```m
Type.FunctionRequiredParameters(type function (x as number, y as text) as any)
```

```text
2
```

An `optional` parameter does not raise the required count.

```m
Type.FunctionRequiredParameters(type function (x as number, optional y as text) as any)
```

```text
1
```

A function whose parameters are all optional requires none.

```m
Type.FunctionRequiredParameters(type function (optional x as number, optional y as text) as any)
```

```text
0
```

## Type.FunctionReturn

These examples show the return type reported for functions with optional or nullable parameters and nullable or structured results.

```m
Type.FunctionReturn(type function (value as nullable text, optional count as number) as number)
```

```text
type number
```

```m
Type.FunctionReturn(type function (value as text) as nullable number)
```

```text
type nullable number
```

```m
Type.FunctionReturn(type function (value as number) as table [Name = text, Score = number])
```

```text
type table [Name = text, Score = number]
```

## Type.Is

Nullability is part of the check, and `null` has its own type.

```m
Type.Is(type number, type nullable number)
```

```text
true
```

```m
Type.Is(type nullable number, type number)
```

```text
false
```

```m
Type.Is(type null, type nullable number)
```

```text
true
```

## Type.IsNullable

Nullability is a flag on the type itself, which is not the same as whether the type admits null values.

```m
Type.IsNullable(type number)
```

```text
false
```

```m
Type.IsNullable(type nullable number)
```

```text
true
```

```m
Type.IsNullable(type any)
```

```text
true
```

## Type.IsOpenRecord

These examples show that only the trailing `...` makes a record type open, while an `optional` field does not.

```m
Type.IsOpenRecord(type [A = number, ...])
```

```text
true
```

```m
Type.IsOpenRecord(type [A = number, optional B = text])
```

```text
false
```

```m
Type.IsOpenRecord(type [A = number])
```

```text
false
```

## Type.ListItem

The item type retains nullability.

```m
Type.ListItem(type {nullable number})
```

```text
type nullable number
```

A plain `type list` has items of type `any`.

```m
Type.ListItem(type list)
```

```text
type any
```

Nested list types return the inner list type.

```m
Type.ListItem(type {{number}})
```

```text
type {number}
```

## Type.NonNullable

The examples show that `Type.NonNullable` removes only the outer `nullable` marker, leaving an already non-nullable type and any element nullability untouched.

```m
Type.NonNullable(type nullable number)
```

```text
type number
```

```m
Type.NonNullable(type number)
```

```text
type number
```

```m
Type.NonNullable(type nullable {nullable number})
```

```text
type {nullable number}
```

## Type.OpenRecord

Opening a record type adds an open marker to the outer type without changing its field types.

Opening preserves field types, including nullable ones.

```m
Type.OpenRecord(type [A = number, B = nullable text])
```

```text
type [A = number, B = nullable text, ...]
```

An already-open record type is returned unchanged.

```m
Type.OpenRecord(type [A = number, ...])
```

```text
type [A = number, ...]
```

Opening is shallow: a nested record used as a field type stays closed.

```m
Type.OpenRecord(type [Outer = [Inner = number]])
```

```text
type [Outer = [Inner = number], ...]
```

## Type.RecordFields

Optional fields are flagged separately from `nullable`, which stays inside each field's `Type`.

```m
Type.RecordFields(type [A = number, optional B = any])
```

```text
[A = [Type = type number, Optional = false], B = [Type = type any, Optional = true]]
```

```m
Type.RecordFields(type [A = nullable text, optional B = nullable text])
```

```text
[A = [Type = type nullable text, Optional = false], B = [Type = type nullable text, Optional = true]]
```

```m
Type.RecordFields(type [])
```

```text
[]
```

## Type.ReplaceFacets

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

## Type.ReplaceTableKeys

Replace, clear, and validate the keys declared on a table type.

```m
Type.TableKeys(Type.ReplaceTableKeys(type table [ID = number, FirstName = text, LastName = text], {[Columns = {"ID"}, Primary = true], [Columns = {"FirstName", "LastName"}, Primary = false]}))
```

```text
{[Columns = {"ID"}, Primary = true], [Columns = {"FirstName", "LastName"}, Primary = false]}
```

```m
Type.TableKeys(Type.ReplaceTableKeys(Type.AddTableKey(type table [ID = number, Name = text], {"ID"}, true), {}))
```

```text
{}
```

```m
Type.TableKeys(Type.ReplaceTableKeys(type table [ID = number], {[Columns = {"Missing"}, Primary = true]}))
```

```text
error: Expression.Error: The column 'Missing' of the table wasn't found. | Detail: "Missing"
```

## Type.ReplaceTablePartitionKey

The partition key is stored on the table type; null clears it, and an empty list reads back as null too.

```m
Type.TablePartitionKey(
    Type.ReplaceTablePartitionKey(type table [Country = text, City = text], {"Country"})
)
```

```text
{"Country"}
```

```m
Type.TablePartitionKey(
    Type.ReplaceTablePartitionKey(
        Type.ReplaceTablePartitionKey(type table [Country = text, City = text], {"Country"}),
        {"City"}
    )
)
```

```text
{"City"}
```

```m
[
    Cleared = Type.TablePartitionKey(
        Type.ReplaceTablePartitionKey(type table [Country = text, City = text], null)
    ),
    Empty = Type.TablePartitionKey(
        Type.ReplaceTablePartitionKey(type table [Country = text, City = text], {})
    )
]
```

```text
[Cleared = null, Empty = null]
```

## Type.TableColumn

These examples show how nullability is preserved and how missing or null column names behave.

```m
Type.TableColumn(type table [A = nullable text, B = number], "A")
```

```text
type nullable text
```

```m
try Type.TableColumn(type table [A = text], "B") otherwise "column not found"
```

```text
"column not found"
```

```m
try Type.TableColumn(type table [A = text], null) otherwise "column name cannot be null"
```

```text
"column name cannot be null"
```

## Type.TableKeys

A table type with no keys returns an empty list, not null.

```m
Type.TableKeys(type table [ID = number, Name = text])
```

```text
{}
```

A table type can carry more than one key, and only one is marked primary.

```m
let
    Base = type table [ID = number, Email = text, Name = text],
    WithID = Type.AddTableKey(Base, {"ID"}, true),
    WithEmail = Type.AddTableKey(WithID, {"Email"}, false)
in
    Type.TableKeys(WithEmail)
```

```text
{[Columns = {"ID"}, Primary = true], [Columns = {"Email"}, Primary = false]}
```

A key can span several columns, so `Columns` is a list rather than a single name.

```m
Type.TableKeys(Type.AddTableKey(type table [Region = text, Store = number], {"Region", "Store"}, true))
```

```text
{[Columns = {"Region", "Store"}, Primary = true]}
```

## Type.TablePartitionKey

A table type with no partition-key facet returns null, while one set with Type.ReplaceTablePartitionKey comes back as a list.

```m
Type.TablePartitionKey(type table [A = nullable number, B = nullable text])
```

```text
null
```

```m
Type.TablePartitionKey(Type.ReplaceTablePartitionKey(type table [A = number, B = text], {"A"}))
```

```text
{"A"}
```

## Type.TableRow

These examples show that the row type keeps a column's nullability, is derived from a table's type rather than its rows, and exists even when the table has no columns.

```m
Type.TableRow(type table [A = number, B = nullable text])
```

```text
type [A = number, B = nullable text]
```

```m
Type.TableRow(Value.Type(#table(type table [A = nullable number], {{null}, {1}})))
```

```text
type [A = nullable number]
```

```m
Type.TableRow(Value.Type(#table({}, {})))
```

```text
type []
```

## Type.TableSchema

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

## Type.Union

These examples show how Type.Union treats nullability, incompatible primitives, and an empty list.

```m
Type.Union({type text, type nullable text})
```

```text
type nullable text
```

```m
Type.Union({type text, type number})
```

```text
type any
```

```m
Type.Union({})
```

```text
type none
```
