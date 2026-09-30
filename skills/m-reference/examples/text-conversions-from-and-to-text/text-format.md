<!-- lab: desktop 2.157.879.0 -->

# Text.Format

Positional arguments from a list, named ones from a record.

```m
{Text.Format("#{0} of #{1}", {3, 10}), Text.Format("#[name] is #[age]", [name = "Ana", age = 30])}
```

```text
{"3 of 10", "Ana is 30"}
```
