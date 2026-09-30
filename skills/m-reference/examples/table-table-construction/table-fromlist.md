<!-- lab: desktop 2.157.879.0 -->

# Table.FromList

Split each item into columns.

```m
Table.FromList({"a,1", "b,2"}, Splitter.SplitTextByDelimiter(","), {"k", "v"})
```

```text
#table(type table [k = nullable text, v = nullable text], {{"a", "1"}, {"b", "2"}})
```
