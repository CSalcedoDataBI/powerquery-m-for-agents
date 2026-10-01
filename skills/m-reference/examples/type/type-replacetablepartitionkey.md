<!-- lab: desktop 2.157.879.0 -->

# Type.ReplaceTablePartitionKey

The partition key is stored on the table type; null clears it, and an empty list reads back as null too.

```m
Type.TablePartitionKey(
    Type.ReplaceTablePartitionKey(type table [Country = text, City = text], {"Country"})
)
```

```text
{"Country"}
```

```m
Type.TablePartitionKey(
    Type.ReplaceTablePartitionKey(
        Type.ReplaceTablePartitionKey(type table [Country = text, City = text], {"Country"}),
        {"City"}
    )
)
```

```text
{"City"}
```

```m
[
    Cleared = Type.TablePartitionKey(
        Type.ReplaceTablePartitionKey(type table [Country = text, City = text], null)
    ),
    Empty = Type.TablePartitionKey(
        Type.ReplaceTablePartitionKey(type table [Country = text, City = text], {})
    )
]
```

```text
[Cleared = null, Empty = null]
```
