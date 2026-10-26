<!-- lab: desktop 2.157.879.0 -->

# Executed examples: text-extraction

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Text.At

The character at a zero-based position.

```m
Text.At("Hello", 1)
```

```text
"e"
```

## Text.End

The last characters.

```m
Text.End("Hello", 2)
```

```text
"lo"
```

## Text.Middle

Past the end it returns what is there, even nothing, instead of an error.

```m
{Text.Middle("Hello", 1, 3), Text.Middle("Hello", 3, 10), Text.Middle("Hello", 10, 2)}
```

```text
{"ell", "lo", ""}
```

## Text.Range

Unlike Text.Middle, an offset past the end is an error.

```m
{Text.Range("Hello", 1, 3), Text.Range("Hello", 10)}
```

```text
{"ell", error: Expression.Error: The 'offset' argument is out of range. | Detail: 10}
```

## Text.Start

The first characters.

```m
Text.Start("Hello", 2)
```

```text
"He"
```
