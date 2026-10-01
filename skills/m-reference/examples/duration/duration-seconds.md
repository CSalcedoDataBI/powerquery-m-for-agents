<!-- lab: desktop 2.157.879.0 -->

# Duration.Seconds

A null duration gives null.

```m
Duration.Seconds(null)
```

```text
null
```

Only the seconds component is returned, however large the other parts are.

```m
Duration.Seconds(#duration(2, 10, 30, 45))
```

```text
45
```

Seconds past a full minute are carried into the minutes first, so the result stays below 60.

```m
Duration.Seconds(#duration(0, 0, 0, 90))
```

```text
30
```
