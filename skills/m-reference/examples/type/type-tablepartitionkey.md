<!-- lab: desktop 2.157.879.0 -->

# Type.TablePartitionKey

A table type with no partition-key facet returns null, while one set with Type.ReplaceTablePartitionKey comes back as a list.

```m
Type.TablePartitionKey(type table [A = nullable number, B = nullable text])
```

```text
null
```

```m
Type.TablePartitionKey(Type.ReplaceTablePartitionKey(type table [A = number, B = text], {"A"}))
```

```text
{"A"}
```
