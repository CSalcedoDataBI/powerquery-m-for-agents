<!-- lab: desktop 2.157.879.0 -->

# Types and metadata

Every value has a type, read with `Value.Type` and tested with `is`. A text that looks like a
number is still text.

```m
{Value.Type(1), 1 is number, "1" is number, null is nullable number}
```

```text
{type number, true, false, true}
```

## A type on a table is a claim, not a conversion

Declaring a column as `number` does not convert or check what is in it. The text stays text
until something that needs a number reads it.

```m
let
    T = #table(type table [x = number], {{"not a number"}})
in
    {T{0}[x], Value.Type(T)}
```

```text
{"not a number", type table [x = number]}
```

Converting is a step of its own, and it is where a bad value becomes an error.

```m
Table.TransformColumnTypes(#table({"x"}, {{"1"}, {"x"}}), {{"x", type number}})
```

```text
#table(type table [x = nullable number], {{1}, {error: DataFormat.Error: We couldn't convert to Number. | Detail: "x"}})
```

## Int64.Type and friends are number, named by metadata

`Int64.Type`, `Currency.Type` and `Percentage.Type` are compatible with `number` (`Type.Is`
says so) but not equal to it. The name that tells them apart lives in the metadata on the
type, which Power BI reads when it loads a column.

```m
{Int64.Type = type number, Type.Is(Int64.Type, type number), Value.Metadata(Int64.Type)}
```

```text
{false, true, [#"Documentation.Name" = "Int64.Type", #"Documentation.Description" = "The type that represents signed 64 bit integer.", #"Documentation.LongDescription" = "The type that represents signed 64 bit integer.", #"Documentation.Category" = "", #"Documentation.Examples" = {}]}
```

## Metadata on any value

`meta` attaches a record to a value without changing the value; `Value.Metadata` reads it back.

```m
let v = 1 meta [Source = "lab"] in {v + 1, Value.Metadata(v)}
```

```text
{2, [Source = "lab"]}
```

## Function types

A function's type lists its parameters. An `optional` parameter is also nullable, whatever
type it was declared with.

```m
Value.Type((x as number, optional y as text) => x)
```

```text
type function (x as number, optional y as nullable text) as any
```

A declared parameter type is checked when the function is called.

```m
((x as number) => x)("1")
```

```text
error: Expression.Error: We cannot convert the value "1" to type Number. | Detail: [Value = "1", Type = type number]
```
