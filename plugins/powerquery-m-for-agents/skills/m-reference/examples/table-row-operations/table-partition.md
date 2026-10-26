<!-- lab: desktop 2.157.879.0 -->

# Table.Partition

Rows spread over two tables by a hash of the column.

```m
Table.Partition(#table({"n"}, {{1}, {2}, {3}, {4}}), "n", 2, each _)
```

```text
{#table(type table [n = any], {{2}, {4}}), #table(type table [n = any], {{1}, {3}})}
```
