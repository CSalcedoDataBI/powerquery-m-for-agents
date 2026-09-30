// runner.pq - evaluates every ```m block of the skills in the engine and renders each result
// as M literal text, so a page can quote what the engine returned instead of what we expect.
//
// run_examples.py replaces the Cases line with the blocks it collected and builds a PBIP
// whose only partition is this query. It also replaces the Allowed line with the names
// m_blocks.allowed_names lets a block use, and each case is evaluated with Expression.Evaluate
// over those members of #shared only: no data sources, no connectors, no other queries, no
// Expression.Evaluate - even for a name m_blocks.unsafe_calls could not see.
let
    Cases = {},
    Allowed = {},
    Environment = Record.SelectFields(#shared, Allowed, MissingField.Ignore),

    // A text as an M text literal: "#(" first, so the escapes added after it stay single.
    Quote = (t as text) as text =>
        let
            s1 = Text.Replace(t, "#(#)(", "#(#)(#)("),
            s2 = Text.Replace(s1, """", """"""),
            s3 = Text.Replace(s2, "#(cr)", "#(#)(cr)"),
            s4 = Text.Replace(s3, "#(lf)", "#(#)(lf)"),
            s5 = Text.Replace(s4, "#(tab)", "#(#)(tab)")
        in
            """" & s5 & """",

    Keywords = {"and", "as", "each", "else", "error", "false", "if", "in", "is", "let", "meta",
        "not", "null", "or", "otherwise", "section", "shared", "then", "true", "try", "type"},
    IdentChars = {"A".."Z", "a".."z", "0".."9", "_"},
    Ident = (name as text) as text =>
        if name <> "" and Text.Select(name, IdentChars) = name
            and not List.Contains({"0".."9"}, Text.Start(name, 1))
            and not List.Contains(Keywords, name)
        then name
        else "#" & Quote(name),

    Num = (n as number) as text =>
        if Number.IsNaN(n) then "#nan"
        else if n = Number.PositiveInfinity then "#infinity"
        else if n = Number.NegativeInfinity then "-#infinity"
        else try Number.ToText(n, "R", "en-US") otherwise Number.ToText(n, null, "en-US"),

    // Int64.Type, Currency.Type and friends are `number` with no facets set: what names them
    // is Documentation.Name in their metadata. Printed only when #shared has that name, so a
    // result can never show a type name the library does not export.
    TypeName = (t as type) as nullable text =>
        let
            n = Record.FieldOrDefault(Value.Metadata(t), "Documentation.Name", null)
        in
            if n is text and Text.EndsWith(n, ".Type") and Record.HasFields(#shared, n)
            then n else null,

    Primitive = (t as type) as text =>
        let
            candidates = {
                {type logical, "logical"}, {type number, "number"}, {type time, "time"},
                {type date, "date"}, {type datetime, "datetime"},
                {type datetimezone, "datetimezone"}, {type duration, "duration"},
                {type text, "text"}, {type binary, "binary"}, {type type, "type"},
                {type list, "list"}, {type record, "record"}, {type table, "table"},
                {type function, "function"}, {type anynonnull, "any"}
            },
            hit = List.First(List.Select(candidates, each Type.Is(t, _{0})), null)
        in
            if Type.Is(t, type none) then "none" else if hit = null then "any" else hit{1},

    FieldsText = (fields as record, open as logical) as text =>
        let
            names = Record.FieldNames(fields),
            parts = List.Transform(names, (n) =>
                let f = Record.Field(fields, n) in
                    (if f[Optional] then "optional " else "") & Ident(n) & " = " & TypeText(f[Type])),
            all = if open then parts & {"..."} else parts
        in
            "[" & Text.Combine(all, ", ") & "]",

    FunctionTypeText = (t as type) as text =>
        let
            params = Type.FunctionParameters(t),
            names = Record.FieldNames(params),
            required = Type.FunctionRequiredParameters(t),
            parts = List.Transform(List.Positions(names), (i) =>
                (if i >= required then "optional " else "") & Ident(names{i}) & " as "
                    & TypeText(Record.Field(params, names{i})))
        in
            "function (" & Text.Combine(parts, ", ") & ") as " & TypeText(Type.FunctionReturn(t)),

    TypeText = (t as type) as text =>
        let
            nullable = Type.IsNullable(t) and not Type.Is(t, type null),
            base = Type.NonNullable(t),
            named = TypeName(t),
            body =
                if Type.Is(t, type null) then "null"
                else if named <> null then named
                else if Type.Is(base, type table) then
                    "table " & FieldsText(Type.RecordFields(Type.TableRow(base)), false)
                else if Type.Is(base, type record) then
                    FieldsText(Type.RecordFields(base), Type.IsOpenRecord(base))
                // A let binding that calls itself needs @; without it the engine reports
                // "The import TypeText matches no exports".
                else if Type.Is(base, type list) then "{" & @TypeText(Type.ListItem(base)) & "}"
                else if Type.Is(base, type function) then FunctionTypeText(base)
                else Primitive(base),
            // `any` includes null; the same type without null is spelled anynonnull.
            spelled = if body = "any" and not Type.IsNullable(t) then "anynonnull" else body
        in
            (if nullable and body <> "any" then "nullable " else "") & spelled,

    ErrorText = (e as record) as text =>
        let
            detail = Record.FieldOrDefault(e, "Detail", null),
            detailText = if detail = null then "" else " | Detail: " & Safe(() => detail)
        in
            "error: " & OrEmpty(e[Reason]) & ": " & OrEmpty(e[Message]) & detailText,
    OrEmpty = (x as any) as text => if x is null then "" else Text.From(x),

    // Every nested value is rendered through Safe with a thunk, so an error in one cell shows
    // as that cell's text instead of failing the whole case.
    Safe = (get as function) as text =>
        let r = try Render(get()) in if r[HasError] then ErrorText(r[Error]) else r[Value],

    MaxItems = 100,
    ListText = (items as list) as text =>
        let
            head = List.FirstN(items, MaxItems + 1),
            shown = List.FirstN(head, MaxItems),
            parts = List.Transform(List.Positions(shown), (i) => Safe(() => shown{i})),
            more = if List.Count(head) > MaxItems then {"..."} else {}
        in
            "{" & Text.Combine(parts & more, ", ") & "}",

    TableText = (t as table) as text =>
        let
            head = Table.FirstN(t, MaxItems + 1),
            shown = Table.FirstN(head, MaxItems),
            columns = Table.ColumnNames(t),
            rows = List.Transform(Table.ToRecords(shown), (r) =>
                "{" & Text.Combine(List.Transform(columns, (c) => Safe(() => Record.Field(r, c))), ", ")
                    & "}"),
            more = if Table.RowCount(head) > MaxItems then {"..."} else {}
        in
            "#table(type " & TypeText(Value.Type(t)) & ", {" & Text.Combine(rows & more, ", ") & "})",

    Render = (v as any) as text =>
        if v is null then "null"
        else if v is logical then (if v then "true" else "false")
        else if v is number then Num(v)
        else if v is text then Quote(v)
        else if v is date then
            "#date(" & Text.Combine(List.Transform({Date.Year(v), Date.Month(v), Date.Day(v)}, Num), ", ") & ")"
        else if v is datetimezone then
            "#datetimezone(" & Text.Combine(List.Transform({Date.Year(v), Date.Month(v), Date.Day(v),
                Time.Hour(v), Time.Minute(v), Time.Second(v),
                DateTimeZone.ZoneHours(v), DateTimeZone.ZoneMinutes(v)}, Num), ", ") & ")"
        else if v is datetime then
            "#datetime(" & Text.Combine(List.Transform({Date.Year(v), Date.Month(v), Date.Day(v),
                Time.Hour(v), Time.Minute(v), Time.Second(v)}, Num), ", ") & ")"
        else if v is time then
            "#time(" & Text.Combine(List.Transform({Time.Hour(v), Time.Minute(v), Time.Second(v)}, Num), ", ") & ")"
        else if v is duration then
            "#duration(" & Text.Combine(List.Transform({Duration.Days(v), Duration.Hours(v),
                Duration.Minutes(v), Duration.Seconds(v)}, Num), ", ") & ")"
        else if v is binary then
            "#binary({" & Text.Combine(List.Transform(Binary.ToList(v), Num), ", ") & "})"
        else if v is list then ListText(v)
        else if v is record then
            "[" & Text.Combine(List.Transform(Record.FieldNames(v), (f) =>
                Ident(f) & " = " & Safe(() => Record.Field(v, f))), ", ") & "]"
        else if v is table then TableText(v)
        else if v is type then "type " & TypeText(v)
        else if v is function then FunctionTypeText(Value.Type(v))
        else "<" & Primitive(Value.Type(v)) & ">",

    // Separate Expression.Evaluate calls share cached values: with the same #table literal in
    // two cases, Table.TransformColumnNames in one made Table.Buffer in the other return the
    // renamed columns (reproduced 2026-09-29; one query with both steps is not affected). A
    // distinct environment per case is meant to keep each evaluation to itself.
    Run = (i as number, code as text) as text =>
        let r = try Render(Expression.Evaluate(code, Environment & [#"__runner case" = i])) in
            if r[HasError] then ErrorText(r[Error]) else r[Value],

    Result = #table(
        type table [seq = Int64.Type, id = text, result = text],
        List.Transform(List.Positions(Cases), (i) => {i, Cases{i}{0}, Run(i, Cases{i}{1})})
    )
in
    Result
