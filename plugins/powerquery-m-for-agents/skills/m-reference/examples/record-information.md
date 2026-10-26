<!-- lab: desktop 2.157.879.0 -->

# Executed examples: record-information

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Record.FieldCount

Fields holding null still count, an empty record has no fields, and a nested record counts as a single field.

```m
Record.FieldCount([Name = "Bob", MiddleName = null, Nickname = null])
```

```text
3
```

```m
Record.FieldCount([])
```

```text
0
```

```m
Record.FieldCount([Outer = [Inner1 = 1, Inner2 = 2]])
```

```text
1
```

## Record.HasFields

Shows how null field values, missing names in a list, and case mismatches are handled.

```m
Record.HasFields([CustomerID = null, Name = "Bob"], "CustomerID")
```

```text
true
```

```m
Record.HasFields([CustomerID = 1, Name = "Bob"], {"CustomerID", "Address"})
```

```text
false
```

```m
Record.HasFields([Name = "Bob"], "name")
```

```text
false
```
