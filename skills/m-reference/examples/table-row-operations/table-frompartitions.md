<!-- lab: desktop 2.157.879.0 -->

# Table.FromPartitions

Tables stacked, each tagged with its partition value.

```m
Table.FromPartitions("Year", {{2023, #table({"v"}, {{1}})}, {2024, #table({"v"}, {{2}})}}, Int64.Type)
```

```text
#table(type table [v = any, Year = Int64.Type], {{1, 2023}, {2, 2024}})
```
