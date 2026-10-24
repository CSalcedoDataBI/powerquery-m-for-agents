<!-- lab: desktop 2.159.883.0 -->

# Function.From

The wrapped function receives every argument as one list, including omitted optional ones, and the declared parameter types may not be checked.

```m
Function.From(type function (a as number, b as number) as number, List.Sum)(2, 1)
```

```text
3
```

When an optional parameter is omitted, this shows whether the list holds a null for it or is shorter.

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
