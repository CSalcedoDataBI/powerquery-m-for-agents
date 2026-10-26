<!-- lab: desktop 2.157.879.0 -->

# Executed examples: table-transformation

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Table.AddColumn

With the fourth argument the column is typed; without it, it is any.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Value.Type(Table.AddColumn(T, "D", each [Qty] * 2, Int64.Type)), Value.Type(Table.AddColumn(T, "D", each [Qty] * 2))}
```

```text
{type table [Name = text, Qty = Int64.Type, D = Int64.Type], type table [Name = text, Qty = Int64.Type, D = any]}
```

## Table.AddFuzzyClusterColumn

The column must be typed as text: a #table with bare column names is not.

```m
Table.AddFuzzyClusterColumn(#table({"City"}, {{"Seattle"}, {"seattle"}}), "City", "Cluster")
```

```text
error: Expression.Error: We only support text columns for fuzzy join operations. The column 'City' is not of type text.
```

Typed as text, similar spellings get one cluster value.

```m
Table.AddFuzzyClusterColumn(#table(type table [City = text], {{"Seattle"}, {"seattle"}, {"Seatle"}, {"Redmond"}}), "City", "Cluster")
```

```text
#table(type table [City = text, Cluster = text], {{"Seattle", "Seattle"}, {"seattle", "Seattle"}, {"Seatle", "Seattle"}, {"Redmond", "Redmond"}})
```

## Table.AddIndexColumn

An index from 1.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.AddIndexColumn(T, "Index", 1, 1, Int64.Type)
```

```text
#table(type table [Name = text, Qty = Int64.Type, Index = Int64.Type], {{"a", 1, 1}, {"b", 2, 2}, {"a", 3, 3}})
```

## Table.AddJoinColumn

A nested table of matches per row; empty when none.

```m
Table.AddJoinColumn(#table({"Id"}, {{1}, {2}}), "Id", #table({"Id", "V"}, {{1, "x"}}), "Id", "Match")
```

```text
#table(type table [Id = any, Match = table [Id = any, V = any]], {{1, #table(type table [Id = any, V = any], {{1, "x"}})}, {2, #table(type table [Id = any, V = any], {})}})
```

## Table.AddKey

The key is metadata: rows are not checked.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Keys(Table.AddKey(T, {"Name"}, true))
```

```text
{[Columns = {"Name"}, Primary = true]}
```

## Table.AggregateTableColumn

Aggregate a nested table column into a new column.

```m
Table.AggregateTableColumn(#table({"G", "T"}, {{"x", #table({"v"}, {{1}, {2}})}}), "T", {{"v", List.Sum, "Total"}})
```

```text
#table(type table [G = any, Total = any], {{"x", 3}})
```

## Table.ClearDown

A value repeated from the row above is cleared.

```m
Table.ClearDown(#table({"G", "v"}, {{"a", 1}, {"a", 2}, {"b", 3}}), {"G"})
```

```text
#table(type table [G = any, v = any], {{"a", 1}, {null, 2}, {"b", 3}})
```

## Table.CombineColumns

Two columns into one text.

```m
Table.CombineColumns(#table({"F", "L"}, {{"Ana", "Diaz"}}), {"F", "L"}, Combiner.CombineTextByDelimiter(" "), "Full")
```

```text
#table(type table [Full = text], {{"Ana Diaz"}})
```

## Table.CombineColumnsToRecord

Two columns into one record column.

```m
Table.CombineColumnsToRecord(#table({"a", "b"}, {{1, 2}}), "R", {"a", "b"})
```

```text
#table(type table [R = [a = any, b = any]], {{[a = 1, b = 2]}})
```

## Table.ConformToPageReader

Called directly with an identity function, the table comes back unchanged.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ConformToPageReader(T, each _)
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
```

## Table.ExpandListColumn

One row per list item; an empty list leaves a null row.

```m
Table.ExpandListColumn(#table({"k", "v"}, {{"a", {1, 2}}, {"b", {}}}), "v")
```

```text
#table(type table [k = any, v = any], {{"a", 1}, {"a", 2}, {"b", null}})
```

## Table.ExpandRecordColumn

Pick fields and name the new columns.

```m
Table.ExpandRecordColumn(#table({"r"}, {{[x = 1, y = 2]}}), "r", {"x"}, {"r.x"})
```

```text
#table(type table [#"r.x" = any], {{1}})
```

## Table.ExpandTableColumn

One row per nested row.

```m
Table.ExpandTableColumn(#table({"k", "t"}, {{"a", #table({"v"}, {{1}, {2}})}}), "t", {"v"})
```

```text
#table(type table [k = any, v = any], {{"a", 1}, {"a", 2}})
```

## Table.FillDown

Nulls take the value above.

```m
Table.FillDown(#table({"G", "v"}, {{"a", 1}, {null, 2}, {"b", 3}}), {"G"})
```

```text
#table(type table [G = any, v = any], {{"a", 1}, {"a", 2}, {"b", 3}})
```

## Table.FillUp

Nulls take the value below.

```m
Table.FillUp(#table({"G", "v"}, {{null, 1}, {"a", 2}}), {"G"})
```

```text
#table(type table [G = any, v = any], {{"a", 1}, {"a", 2}})
```

## Table.FuzzyGroup

The key column must be typed as text.

```m
Table.FuzzyGroup(#table({"City"}, {{"Seattle"}}), "City", {{"Count", each Table.RowCount(_), Int64.Type}})
```

```text
error: Expression.Error: We only support text columns for fuzzy join operations. The column 'City' is not of type text.
```

Typed as text, similar spellings are grouped together.

```m
Table.FuzzyGroup(#table(type table [City = text], {{"Seattle"}, {"seattle"}, {"Redmond"}}), "City", {{"Count", each Table.RowCount(_), Int64.Type}})
```

```text
#table(type table [City = text, Count = Int64.Type], {{"Seattle", 2}, {"Redmond", 1}})
```

## Table.FuzzyJoin

Key columns must be typed as text.

```m
Table.FuzzyJoin(#table({"A"}, {{"Seattle"}}), {"A"}, #table({"B"}, {{"seattle"}}), {"B"})
```

```text
error: Expression.Error: We only support text columns for fuzzy join operations. The column 'A' is not of type text.
```

Typed as text, a case difference still matches.

```m
Table.FuzzyJoin(#table(type table [A = text], {{"Seattle"}}), {"A"}, #table(type table [B = text], {{"seattle"}, {"Redmond"}}), {"B"})
```

```text
#table(type table [A = text, B = text], {{"Seattle", "seattle"}})
```

## Table.FuzzyNestedJoin

Key columns must be typed as text; the error surfaces inside the nested column.

```m
Table.FuzzyNestedJoin(#table({"A"}, {{"Seattle"}}), {"A"}, #table({"B"}, {{"seattle"}}), {"B"}, "M")
```

```text
#table(type table [A = any, M = nullable table [B = any]], {{"Seattle", error: Expression.Error: We only support text columns for fuzzy join operations. The column 'B' is not of type text.}})
```

Typed as text, the matches arrive as a nested table.

```m
Table.FuzzyNestedJoin(#table(type table [A = text], {{"Seattle"}}), {"A"}, #table(type table [B = text], {{"seattle"}, {"Redmond"}}), {"B"}, "M")
```

```text
#table(type table [A = text, M = nullable table [B = text]], {{"Seattle", #table(type table [B = any], {{"seattle"}})}})
```

## Table.Group

Sum per key.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Group(T, {"Name"}, {{"Total", each List.Sum([Qty]), Int64.Type}})
```

```text
#table(type table [Name = text, Total = Int64.Type], {{"a", 4}, {"b", 2}})
```

## Table.Join

A flat join; unmatched left rows get nulls.

```m
Table.Join(#table({"Id", "A"}, {{1, "x"}, {2, "y"}}), "Id", #table({"Key", "B"}, {{1, "p"}}), "Key", JoinKind.LeftOuter)
```

```text
#table(type table [Id = any, A = any, Key = any, B = any], {{1, "x", 1, "p"}, {2, "y", null, null}})
```

## Table.Keys

A table built in memory has no keys.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Keys(T)
```

```text
{}
```

## Table.NestedJoin

The matches as a nested table column, empty when none.

```m
Table.NestedJoin(#table({"Id", "A"}, {{1, "x"}, {2, "y"}}), "Id", #table({"Key", "B"}, {{1, "p"}}), "Key", "Right", JoinKind.LeftOuter)
```

```text
#table(type table [Id = any, A = any, Right = table [Key = any, B = any]], {{1, "x", #table(type table [Key = any, B = any], {{1, "p"}})}, {2, "y", #table(type table [Key = any, B = any], {})}})
```

## Table.PartitionKey

A table built in memory has no partition key.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.PartitionKey(T)
```

```text
null
```

## Table.ReplaceErrorValues

A failed conversion replaced by 0.

```m
Table.ReplaceErrorValues(Table.TransformColumnTypes(#table({"v"}, {{"1"}, {"x"}}), {{"v", Int64.Type}}), {{"v", 0}})
```

```text
#table(type table [v = nullable number], {{1}, {0}})
```

## Table.ReplaceKeys

Replace the key metadata.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Keys(Table.ReplaceKeys(T, {[Columns = {"Name"}, Primary = true]}))
```

```text
{[Columns = {"Name"}, Primary = true]}
```

## Table.ReplacePartitionKey

Set the partition key, then read it back.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.PartitionKey(Table.ReplacePartitionKey(T, {"Name"}))
```

```text
{"Name"}
```

## Table.ReplaceRelationshipIdentity

On a table built in memory, the table comes back unchanged.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.ReplaceRelationshipIdentity(T, "id")
```

```text
#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
```

## Table.ReplaceValue

The replacer decides: the whole value, or part of a text.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    {Table.ReplaceValue(T, "a", "A", Replacer.ReplaceValue, {"Name"}), Table.ReplaceValue(#table({"s"}, {{"banana"}}), "an", "AN", Replacer.ReplaceText, {"s"})}
```

```text
{#table(type table [Name = text, Qty = Int64.Type], {{"A", 1}, {"b", 2}, {"A", 3}}), #table(type table [s = nullable text], {{"bANANa"}})}
```

## Table.Split

Pages of two rows.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.Split(T, 2)
```

```text
{#table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}}), #table(type table [Name = text, Qty = Int64.Type], {{"a", 3}})}
```

## Table.SplitColumn

Split a text column into two.

```m
Table.SplitColumn(#table({"Full"}, {{"Ana Diaz"}}), "Full", Splitter.SplitTextByDelimiter(" "), {"First", "Last"})
```

```text
#table(type table [First = nullable text, Last = nullable text], {{"Ana", "Diaz"}})
```

## Table.TransformColumns

Without a type, the column takes the declared return type of the function: Text.Upper declares nullable text.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Value.Type(Table.TransformColumns(T, {{"Name", Text.Upper}, {"Qty", each _ * 10, Int64.Type}}))
```

```text
type table [Name = nullable text, Qty = Int64.Type]
```

## Table.TransformColumnTypes

The culture decides how the same text reads as a date.

```m
{Table.TransformColumnTypes(#table({"d"}, {{"1/2/2024"}}), {{"d", type date}}, "en-US"), Table.TransformColumnTypes(#table({"d"}, {{"1/2/2024"}}), {{"d", type date}}, "es-ES")}
```

```text
{#table(type table [d = nullable date], {{#date(2024, 1, 2)}}), #table(type table [d = nullable date], {{#date(2024, 2, 1)}})}
```

## Table.TransformRows

A list built from every row.

```m
let
    T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}})
in
    Table.TransformRows(T, each [Name] & Text.From([Qty]))
```

```text
{"a1", "b2", "a3"}
```

## Table.Transpose

Rows become columns.

```m
Table.Transpose(#table({"a", "b"}, {{1, 2}, {3, 4}}))
```

```text
#table(type table [Column1 = any, Column2 = any], {{1, 3}, {2, 4}})
```
