<!-- lab: desktop 2.157.879.0 -->

# Number.FromText and the culture

**What happens:** the culture decides which character is the decimal separator and which one
is a thousands separator that is **silently dropped**. `"1,5"` in en-US is fifteen, not one and
a half, and there is no error to warn you.

```m
{Number.FromText("1.234", "en-US"), Number.FromText("1.234", "es-ES"), Number.FromText("1,5", "en-US"), Number.FromText("1,5", "es-ES")}
```

```text
{1.234, 1234, 15, 1.5}
```

Without a culture argument the query's culture applies - en-US in this lab's model, so the
results match the en-US ones above. On another machine or file it can be a different culture.

```m
{Number.FromText("1.234"), Number.FromText("1,5")}
```

```text
{1.234, 15}
```

**Do this:** always pass the culture of the **data**, not of the machine, to `Number.FromText`
and to `Table.TransformColumnTypes` (★ note there shows the same effect on a whole column).
