<!-- lab: desktop 2.157.879.0 -->

# Executed examples: logical

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Logical.From

The examples show null and logical passthrough, zero-versus-nonzero numbers, and uppercase text.

```m
List.Transform({null, true}, Logical.From)
```

```text
{null, true}
```

```m
List.Transform({0, -1, 0.5}, Logical.From)
```

```text
{false, true, true}
```

```m
Logical.From("TRUE")
```

```text
true
```

## Logical.FromText

These examples show case-insensitive conversion, null handling, and invalid input.

```m
Logical.FromText("TRUE")
```

```text
true
```

```m
Logical.FromText(null)
```

```text
null
```

```m
Logical.FromText("a")
```

```text
error: Expression.Error: We couldn't convert to Logical. | Detail: "a"
```

## Logical.ToText

These examples show the lowercase text produced for a logical value, that null passes through as null, and that a non-logical value raises an error.

```m
Logical.ToText(true)
```

```text
"true"
```

```m
Logical.ToText(null)
```

```text
null
```

```m
Logical.ToText(1)
```

```text
error: Expression.Error: We cannot convert the value 1 to type Logical. | Detail: [Value = 1, Type = type nullable logical]
```
