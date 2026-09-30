<!-- lab: desktop 2.157.879.0 -->

# Table.AlternateRows

Keep the first row, then skip 1 and take 1.

```m
Table.AlternateRows(#table({"n"}, {{1}, {2}, {3}, {4}, {5}}), 1, 1, 1)
```

```text
#table(type table [n = any], {{1}, {3}, {5}})
```
