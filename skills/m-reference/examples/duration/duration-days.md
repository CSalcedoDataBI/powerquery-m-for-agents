<!-- lab: desktop 2.157.879.0 -->

# Duration.Days

The examples show the days portion of a duration, which is not the same as the total number of days.

```m
Duration.Days(#duration(1, 23, 0, 0))
```

```text
1
```

A duration shorter than one whole day has zero days.

```m
Duration.Days(#duration(0, 5, 30, 0))
```

```text
0
```

A null duration gives a null result.

```m
Duration.Days(null)
```

```text
null
```
