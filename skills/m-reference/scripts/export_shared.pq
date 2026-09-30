// export_shared.pq - dumps every library function the engine has loaded, with the
// documentation metadata carried on its type, and every other library member (constants
// such as GroupKind.Local, type values such as Int64.Type) with its value, as JSON.
//
// Paste into a blank query (Power BI Desktop, Excel, Dataflows Gen2). Set Host below.
// The result is a table of JSON chunks: 30,000 characters each, because an Excel cell holds
// 32,767 and the full export is several megabytes. Concatenate `json` in `part` order and
// save it as exports/<host>-<version>.json; sync_shared.py reads that file.
//
// Nothing here is guessed from docs: a member is in the output only if #shared has it.
let
    Host = "desktop",
    // Fill in the host build (Help > About in Desktop). It is stamped into catalog.json.
    HostVersion = "",

    // M has no Type.ToText. Primitive types are compared from specific to general, so
    // `table [a = number]` reads as "table" and Int64.Type (number + facets) as "number".
    TypeName = (t as type) as text =>
        let
            isNullable = Type.IsNullable(t),
            base = Type.NonNullable(t),
            candidates = {
                {type logical, "logical"}, {type number, "number"}, {type time, "time"},
                {type date, "date"}, {type datetime, "datetime"},
                {type datetimezone, "datetimezone"}, {type duration, "duration"},
                {type text, "text"}, {type binary, "binary"}, {type type, "type"},
                {type list, "list"}, {type record, "record"}, {type table, "table"},
                {type function, "function"}, {type anynonnull, "any"}
            },
            hit = List.First(List.Select(candidates, each Type.Is(base, _{0})), null),
            name =
                if Type.Is(base, type none) then (if isNullable then "null" else "none")
                else if hit = null then "any"
                else hit{1}
        in
            if isNullable and name <> "any" and name <> "null" then "nullable " & name else name,

    TextField = (r as record, field as text) as nullable text =>
        let v = Record.FieldOrDefault(r, field, null) in if v is text then v else null,

    // Names below avoid M keywords (`meta`, `type`) and never shadow a field with itself:
    // inside a record literal, `name = name` refers to the field, not to the variable.
    Row = (fnName as text, f as function) as record =>
        let
            t = Value.Type(f),
            docs = Value.Metadata(t),
            params = Type.FunctionParameters(t),
            names = Record.FieldNames(params),
            required = Type.FunctionRequiredParameters(t),
            rawExamples = Record.FieldOrDefault(docs, "Documentation.Examples", {}),
            exampleList =
                if rawExamples is list then rawExamples
                else if rawExamples is record then {rawExamples}
                else {},
            exampleRows = List.Transform(
                List.Select(exampleList, each _ is record),
                each [
                    description = TextField(_, "Description"),
                    code = TextField(_, "Code"),
                    result = TextField(_, "Result")
                ]
            )
        in
            [
                name = fnName,
                category = TextField(docs, "Documentation.Category"),
                description = TextField(docs, "Documentation.Description"),
                longDescription = TextField(docs, "Documentation.LongDescription"),
                parameters = List.Transform(
                    List.Positions(names),
                    (i) => [
                        name = names{i},
                        #"type" = TypeName(Record.Field(params, names{i})),
                        #"optional" = i >= required
                    ]
                ),
                returns = TypeName(Type.FunctionReturn(t)),
                examples = exampleRows
            ],

    // #shared also lists this workbook's own queries. Those are not the library.
    UserMembers = try Record.FieldNames(#sections[Section1]) otherwise {},
    Shared = Record.ToTable(#shared),
    // User members are ruled out BEFORE [Value] is touched: evaluating this query's own
    // member from inside itself is a cyclic reference. `and` short-circuits in M, and the
    // try covers any other member that fails to evaluate.
    Functions = Table.SelectRows(
        Shared,
        each not List.Contains(UserMembers, [Name])
            and (try [Value] is function otherwise false)
    ),
    Rows = List.Transform(
        Table.ToRecords(Functions),
        each try Row([Name], [Value]) otherwise [name = [Name], exportError = true]
    ),

    // Everything else in the library: enum constants (GroupKind.Local = 0), type values
    // (Int64.Type), numbers (Number.PI). `value` is the constant as text, culture-fixed so the
    // export does not depend on the host's locale; null when the member is not a primitive.
    ConstRow = (memberName as text, v as any) as record =>
        let
            docs = Value.Metadata(Value.Type(v)),
            own = Value.Metadata(v)
        in
            [
                name = memberName,
                #"type" = TypeName(Value.Type(v)),
                value = try Text.From(v, "en-US") otherwise null,
                description =
                    let d = TextField(own, "Documentation.Description") in
                        if d <> null then d else TextField(docs, "Documentation.Description")
            ],
    Constants = Table.SelectRows(
        Shared,
        each not List.Contains(UserMembers, [Name])
            and (try not ([Value] is function) otherwise false)
    ),
    ConstRows = List.Transform(
        Table.ToRecords(Constants),
        each try ConstRow([Name], [Value]) otherwise [name = [Name], exportError = true]
    ),

    Payload = [
        host = Host,
        hostVersion = HostVersion,
        exportedAt = DateTimeZone.ToText(DateTimeZone.UtcNow(), [Format = "yyyy-MM-ddTHH:mm:ssZ"]),
        functions = Rows,
        constants = ConstRows
    ],
    Json = Text.FromBinary(Json.FromValue(Payload), TextEncoding.Utf8),
    ChunkSize = 30000,
    Parts = List.Numbers(0, Number.RoundUp(Text.Length(Json) / ChunkSize)),
    Result = #table(
        type table [part = Int64.Type, json = text],
        List.Transform(Parts, each {_, Text.Middle(Json, _ * ChunkSize, ChunkSize)})
    )
in
    Result
