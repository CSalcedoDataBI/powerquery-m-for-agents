<!-- lab: desktop 2.157.879.0 -->

# Number.Combinations

The examples show null arguments and the boundary case of choosing no items.

```m
Number.Combinations(null, 3)
```

```text
null
```

```m
Number.Combinations(5, null)
```

```text
null
```

```m
Number.Combinations(5, 0)
```

```text
1
```

A subset larger than the set is zero ways, not an error.

```m
Number.Combinations(2, 3)
```

```text
0
```
