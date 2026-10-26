<!-- lab: desktop 2.157.879.0 -->

# Table.FromValue

A scalar and a record.

```m
{Table.FromValue(5), Table.FromValue([a = 1, b = 2])}
```

```text
{#table(type table [Value = number], {{5}}), #table(type table [Name = text, Value = any], {{"a", 1}, {"b", 2}})}
```
