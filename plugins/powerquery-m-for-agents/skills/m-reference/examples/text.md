<!-- lab: desktop 2.157.879.0 -->

# Executed examples: text

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## Text.InferNumberType

It returns a type, not a number.

```m
{Text.InferNumberType("42"), Text.InferNumberType("1.5")}
```

```text
{type number, type number}
```
