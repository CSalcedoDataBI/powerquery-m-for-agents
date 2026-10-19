<!-- lab: desktop 2.158.1304.0 -->

# Table.Profile on columns without a type

**What happens:** on a column whose type is `any` - the normal case for a raw CSV or Excel
source before `Table.TransformColumnTypes` - `Table.Profile` leaves `Min`, `Max`, `Average`,
`StandardDeviation` and `DistinctCount` empty. `Count` and `NullCount` are filled, and there is
no error to warn you.

```m
let t = #table({"a", "b"}, {{1, "x"}, {2, null}}) in Table.Profile(t)
```

```text
#table(type table [Column = Text.Type, Min = any, Max = any, Average = any, StandardDeviation = nullable number, Count = number, NullCount = any, DistinctCount = any], {{"a", null, null, null, null, 2, 0, null}, {"b", null, null, null, null, 2, 1, null}})
```

The same values with column types:

```m
let t = #table(type table [a = number, b = text], {{1, "x"}, {2, null}}) in Table.Profile(t)
```

```text
#table(type table [Column = Text.Type, Min = any, Max = any, Average = any, StandardDeviation = nullable number, Count = number, NullCount = any, DistinctCount = any], {{"a", 1, 2, 1.5, 0.70710678118654757, 2, 0, 2}, {"b", "x", "x", null, null, 2, 1, 2}})
```

**Do this:** type the columns before profiling a raw source, or compute the statistics you need
from the column values (`List.Max(t[a])`, `List.Count(List.Distinct(t[b]))`).
