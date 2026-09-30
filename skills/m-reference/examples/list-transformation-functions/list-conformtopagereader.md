<!-- lab: desktop 2.157.879.0 -->

# List.ConformToPageReader

Called directly on a list, it returns a table of one-row tables.

```m
List.ConformToPageReader({1, 2})
```

```text
#table(type table [Result = any], {{#table(type table [Value = number], {{1}})}, {#table(type table [Value = number], {{2}})}})
```
