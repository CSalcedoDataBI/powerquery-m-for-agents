<!-- lab: desktop 2.159.883.0 -->

# Value.Expression

These examples show the tree returned for a plain literal, for null, and for a function value.

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
