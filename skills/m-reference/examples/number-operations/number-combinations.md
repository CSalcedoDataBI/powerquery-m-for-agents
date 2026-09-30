<!-- lab: desktop 2.157.879.0 -->

# Number.Combinations

Order does not matter: subsets of 5 items.

```m
{Number.Combinations(5, 2), Number.Combinations(5, 0), Number.Combinations(5, 5)}
```

```text
{10, 1, 1}
```

A subset larger than the set is zero ways, not an error.

```m
Number.Combinations(2, 3)
```

```text
0
```
