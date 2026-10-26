<!-- lab: desktop 2.157.879.0 -->

# Duration.FromText

Null input returns null, seconds are optional, and a leading day component counts as days.

```m
Duration.FromText(null)
```

```text
null
```

```m
Duration.FromText("01:02")
```

```text
#duration(0, 1, 2, 0)
```

```m
Duration.FromText("1.01:02:03.5")
```

```text
#duration(1, 1, 2, 3.5)
```
