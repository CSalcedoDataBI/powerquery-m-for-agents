<!-- lab: desktop 2.157.879.0 -->

# Table.FromRecords

A missing field is an error unless told to use null.

```m
{Table.FromRecords({[a = 1, b = 2], [a = 3]}, null, MissingField.UseNull), Table.FromRecords({[a = 1, b = 2], [a = 3]})}
```

```text
{#table(type table [a = any, b = any], {{1, 2}, {3, null}}), error: Expression.Error: The field 'b' of the record wasn't found. | Detail: [a = 3]}
```
