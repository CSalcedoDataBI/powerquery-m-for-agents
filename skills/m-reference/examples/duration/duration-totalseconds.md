<!-- lab: desktop 2.157.879.0 -->

# Duration.TotalSeconds

These examples show that fractions of a second are kept, that hours past a day still count, and that a null duration stays null.

```m
Duration.TotalSeconds(#duration(0, 0, 0, 1.5))
```

```text
1.5
```

```m
Duration.TotalSeconds(#duration(0, 25, 0, 0))
```

```text
90000
```

```m
Duration.TotalSeconds(null)
```

```text
null
```
