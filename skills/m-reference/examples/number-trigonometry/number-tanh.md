<!-- lab: desktop 2.159.883.0 -->

# Number.Tanh

The examples show that tanh is odd, that null passes through, and how large or special inputs saturate at ±1.

```m
{Number.Tanh(0), Number.Tanh(1), Number.Tanh(-1), Number.Tanh(0.5)}
```

```text
{0, 0.76159415595576485, -0.76159415595576485, 0.46211715726000974}
```

```m
Number.Tanh(null)
```

```text
null
```

```m
{Number.Tanh(20), Number.Tanh(-1000), Number.Tanh(#infinity), Number.Tanh(-#infinity), Number.Tanh(Number.NaN)}
```

```text
{1, -1, 1, -1, #nan}
```
