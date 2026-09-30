<!-- lab: desktop 2.157.879.0 -->

# Number.Sign

Nulls propagate, zero is its own sign, and a list keeps both behaviours.

```m
Number.Sign(null)
```

```text
null
```

```m
Number.Sign(-0.0)
```

```text
0
```

```m
List.Transform({-2.5, 0, 7, null}, Number.Sign)
```

```text
{-1, 0, 1, null}
```
