<!-- lab: desktop 2.157.879.0 -->

# Record.ToTable

Field order follows the record's definition order, and null values are kept.

```m
Record.ToTable([B = null, A = 1])
```

```text
#table(type table [Name = text, Value = any], {{"B", null}, {"A", 1}})
```

An empty record yields the `Name` and `Value` columns with no rows.

```m
Record.ToTable([])
```

```text
#table(type table [Name = text, Value = any], {})
```

A nested record stays a single record value; it is not flattened into extra rows.

```m
Record.ToTable([A = [X = 1], B = 2])
```

```text
#table(type table [Name = text, Value = any], {{"A", [X = 1]}, {"B", 2}})
```
