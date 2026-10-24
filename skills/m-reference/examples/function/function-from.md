<!-- lab: desktop 2.159.883.0 -->

# Function.From

The wrapped function receives the supplied arguments as one list, and the declared parameter types may not be checked.

```m
Function.From(type function (a as number, b as number) as number, List.Sum)(2, 1)
```

```text
3
```

An omitted optional parameter is absent from the list rather than passed as null, so the list is shorter.

```m
Function.From(type function (a as number, optional b as number) as list, each _)(5)
```

```text
{5}
```

This passes text to a parameter declared `as number`, to show whether the declared type is enforced.

```m
Function.From(type function (a as number) as text, each Text.Upper(_{0}))("abc")
```

```text
"ABC"
```
