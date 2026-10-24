<!-- lab: desktop 2.159.883.0 -->

# Value.Expression

Value.Expression does not resolve a plain value: a literal, null and a function all return the same error asking for `Value.Expression(Value.Optimize(...))` first.

```m
Value.Expression(42)
```

```text
error: Expression.Error: Value.Expression can only resolve optimized expressions, use: Value.Expression(Value.Optimize(...))
```

```m
Value.Expression(null)
```

```text
error: Expression.Error: Value.Expression can only resolve optimized expressions, use: Value.Expression(Value.Optimize(...))
```

```m
Value.Expression(each _ + 1)
```

```text
error: Expression.Error: Value.Expression can only resolve optimized expressions, use: Value.Expression(Value.Optimize(...))
```
