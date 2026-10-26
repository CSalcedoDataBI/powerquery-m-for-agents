<!-- lab: desktop 2.157.879.0 -->

# Executed examples: binary

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Binary.ApproximateLength

A null input returns null rather than 0, and lengths count bytes, not characters.

```m
Binary.ApproximateLength(null)
```

```text
null
```

```m
Binary.ApproximateLength(Binary.FromText("", BinaryEncoding.Base64))
```

```text
0
```

```m
Binary.ApproximateLength(Binary.FromText("aGVsbG8=", BinaryEncoding.Base64))
```

```text
5
```

## Binary.Buffer

Null passes through, empty inputs stay empty, and a buffered value keeps every byte in order.

```m
Binary.Buffer(null)
```

```text
null
```

Buffering an empty binary gives an empty binary, not null.

```m
Binary.Buffer(Binary.FromList({}))
```

```text
#binary({})
```

Zero is a real byte value, so zero bytes survive buffering.

```m
Binary.Buffer(Binary.FromList({0, 0, 255}))
```

```text
#binary({0, 0, 255})
```

## Binary.Combine

Combining binaries concatenates their bytes in list order.

```m
Binary.Combine({Text.ToBinary("ab"), Text.ToBinary("cd")})
```

```text
#binary({97, 98, 99, 100})
```

An empty list produces an empty binary rather than an error.

```m
Binary.Combine({})
```

```text
#binary({})
```

A null item is not skipped or treated as empty; it is rejected.

```m
Binary.Combine({Text.ToBinary("a"), null})
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

## Binary.Compress

Null input comes back as null, and the compression type selects the output container.

```m
Binary.Compress(null, Compression.Deflate)
```

```text
null
```

An empty binary compresses to an empty binary: no header or framing bytes are added.

```m
Binary.Compress(#binary({}), Compression.GZip)
```

```text
#binary({})
```

GZip output starts with the GZip header bytes 31 and 139; a raw deflate stream has no header.

```m
Binary.ToList(Binary.Range(Binary.Compress(Text.ToBinary("Power Query"), Compression.GZip), 0, 2))
```

```text
{31, 139}
```

## Binary.Decompress

A null binary stays null, and the compression type must match the one used to compress the data. A mismatch fails only when the bytes are read, so `try ... otherwise` around the call does not catch it.

```m
Binary.Decompress(null, Compression.Deflate)
```

```text
null
```

```m
Binary.Decompress(Binary.Compress(#binary({1, 2, 3}), Compression.GZip), Compression.GZip)
```

```text
#binary({1, 2, 3})
```

```m
try Binary.Decompress(Binary.Compress(#binary({1, 2, 3}), Compression.GZip), Compression.Deflate) otherwise "wrong compression type"
```

```text
error: DataFormat.Error: Found invalid data while decoding.
```

## Binary.From

These examples show how `Binary.From` treats null, text with an explicit encoding, and an existing binary value.

```m
Binary.From(null)
```

```text
null
```

The optional second argument decodes text using the given encoding instead of the default.

```m
Binary.From("1011", BinaryEncoding.Hex)
```

```text
#binary({16, 17})
```

A binary value is returned unchanged rather than decoded again.

```m
Binary.From(Binary.FromText("1011", BinaryEncoding.Hex))
```

```text
#binary({16, 17})
```

## Binary.FromList

The examples cover an empty list, the 0 and 255 byte boundaries, and a null entry.

```m
Binary.FromList({})
```

```text
#binary({})
```

```m
Binary.FromList({0, 255})
```

```text
#binary({0, 255})
```

```m
Binary.FromList({0, null, 255})
```

```text
error: Expression.Error: We cannot convert the value null to type Number. | Detail: [Value = null, Type = type number]
```

## Binary.FromText

These examples show null propagation and how the same text is decoded differently when the optional encoding argument is omitted versus set to Hex.

```m
Binary.FromText(null)
```

```text
null
```

```m
Binary.FromText("1011")
```

```text
#binary({215, 77, 117})
```

```m
Binary.FromText("1011", BinaryEncoding.Hex)
```

```text
#binary({16, 17})
```

## Binary.InferContentType

Even a short phrase with one comma is reported as CSV, and the record lists every delimiter that
was tried with the columns and rows each would give. A null source is an error.

```m
Binary.InferContentType(Text.ToBinary("Hello, world"))
```

```text
[#"Content.Type" = "text/csv", #"Csv.PotentialDelimiters" = #table(type table [PotentialDelimiter = any, QuoteStyle = any, MaxColumns = any, NonEmptyColumns = any, MaxRows = any, NonEmptyRows = any], {{",", 0, 2, 2, 1, 1}, {",", 1, 2, 2, 1, 1}, {"#(tab)", 0, 1, 1, 1, 1}, {"#(tab)", 1, 1, 1, 1, 1}, {";", 0, 1, 1, 1, 1}, {";", 1, 1, 1, 1, 1}, {":", 0, 1, 1, 1, 1}, {":", 1, 1, 1, 1, 1}, {"|", 0, 1, 1, 1, 1}, {"|", 1, 1, 1, 1, 1}, {"#(0001)", 0, 1, 1, 1, 1}, {"#(0001)", 1, 1, 1, 1, 1}, {"W", 0, 2, 2, 1, 1}, {"W", 1, 2, 2, 1, 1}})]
```

```m
Binary.InferContentType(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

## Binary.Length

Null input returns null, while an empty binary has length zero.

```m
Binary.Length(null)
```

```text
null
```

```m
Binary.Length(Text.ToBinary("Seattle"))
```

```text
7
```

```m
Binary.Length(Text.ToBinary(""))
```

```text
0
```

## Binary.Range

The offset is zero-based, count is optional, and a null count runs to the end of the binary.

```m
Binary.Range(#binary({0..10}), 6)
```

```text
#binary({6, 7, 8, 9, 10})
```

```m
Binary.Range(#binary({0..10}), 6, null)
```

```text
#binary({6, 7, 8, 9, 10})
```

```m
Binary.Range(#binary({0..10}), 6, 0)
```

```text
#binary({})
```

## Binary.Split

Examples cover a short final page, a page size larger than the binary, and a null input.

```m
Binary.Split(Text.ToBinary("abcde"), 2)
```

```text
{#binary({97, 98}), #binary({99, 100}), #binary({101})}
```

```m
Binary.Split(Text.ToBinary("abc"), 5)
```

```text
{#binary({97, 98, 99})}
```

```m
Binary.Split(null, 2)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

## Binary.ToList

The examples show byte-to-number conversion, the empty binary, and null handling.

```m
Binary.ToList(#binary({0x00, 0x7F, 0xFF}))
```

```text
{0, 127, 255}
```

```m
Binary.ToList(#binary({}))
```

```text
{}
```

```m
Binary.ToList(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Binary. | Detail: [Value = null, Type = type binary]
```

## Binary.ToText

The examples show null input, what omitting `encoding` produces, and the Hex alternative.

```m
Binary.ToText(null)
```

```text
null
```

```m
Binary.ToText(Binary.FromList({72, 105}))
```

```text
"SGk="
```

```m
Binary.ToText(Binary.FromList({72, 105}), BinaryEncoding.Hex)
```

```text
"4869"
```

## Binary.View

Handlers are optional, handler errors fall back, and a null binary view needs GetStream.

```m
Binary.Length(Binary.View(Text.ToBinary("hello"), []))
```

```text
5
```

```m
Binary.Length(Binary.View(Text.ToBinary("hello"), [GetLength = () => Number.FromText("not a number")]))
```

```text
5
```

```m
Text.FromBinary(Binary.View(null, [GetLength = () => 12, GetStream = () => Text.ToBinary("hello world!")]))
```

```text
"hello world!"
```

## Binary.ViewError

A null field is allowed, an omitted field is allowed, and a null argument is rejected.

```m
Binary.ViewError([Reason = "Expression.Error", Message = "boom", Detail = null])
```

```text
[Reason = "Expression.Error", Message = "boom", Detail = null]
```

```m
Binary.ViewError([Reason = "Expression.Error", Message = "boom"])
```

```text
[Reason = "Expression.Error", Message = "boom"]
```

```m
Binary.ViewError(null)
```

```text
error: Expression.Error: We cannot convert the value null to type Record. | Detail: [Value = null, Type = type [...]]
```

## Binary.ViewFunction

The examples show a view function running its wrapped function and a Binary.View intercepting or falling back to it.

```m
let
    Size = Binary.ViewFunction((binary as nullable binary) => if binary = null then 0 else Binary.Length(binary))
in
    {Size(null), Size(Text.ToBinary("abcdef"))}
```

```text
{0, 6}
```

When the view supplies an OnInvoke handler, that handler's result is used instead of running the wrapped function.

```m
let
    Size = Binary.ViewFunction((binary as nullable binary) => if binary = null then 0 else Binary.Length(binary)),
    Viewed = Binary.View(
        null,
        [
            GetStream = () => Text.ToBinary("abcdef"),
            OnInvoke = (func, args, index) => 99
        ]
    )
in
    Size(Viewed)
```

```text
99
```

An error raised by OnInvoke is swallowed, and the wrapped function is applied to the view instead.

```m
let
    Size = Binary.ViewFunction((binary as nullable binary) => if binary = null then 0 else Binary.Length(binary)),
    Viewed = Binary.View(
        null,
        [
            GetStream = () => Text.ToBinary("abcdef"),
            GetLength = () => 6,
            OnInvoke = (func, args, index) => error "not handled"
        ]
    )
in
    Size(Viewed)
```

```text
6
```
