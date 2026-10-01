<!-- lab: desktop 2.157.879.0 -->

# Type.ForFunction

The examples show how `min` marks trailing parameters optional and how a nullable parameter type differs from an optional one.

```m
Type.ForFunction([ReturnType = type number, Parameters = [X = type number, Y = type number]], 1)
```

```text
type function (X as number, optional Y as nullable number) as number
```

```m
Type.ForFunction([ReturnType = type nullable number, Parameters = [X = type nullable number]], 1)
```

```text
type function (X as nullable number) as nullable number
```

```m
Type.ForFunction([ReturnType = type logical, Parameters = [X = type logical]], 0)
```

```text
type function (optional X as nullable logical) as logical
```
