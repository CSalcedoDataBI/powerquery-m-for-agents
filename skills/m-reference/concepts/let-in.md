<!-- lab: desktop 2.157.879.0 -->

# let / in

A `let` expression names intermediate values and returns the one after `in`. It reads like a
list of steps, but it is not a sequence: each name is evaluated only when something needs it,
in whatever order that need arises.

Order of the lines does not matter; dependencies do.

```m
let
    b = a * 2,
    a = 5
in
    b
```

```text
10
```

A step nobody uses is never evaluated, so its error never surfaces.

```m
let
    unused = error "never evaluated",
    result = 1
in
    result
```

```text
1
```

Names with spaces or punctuation are quoted identifiers, the form the query editor writes for
every step.

```m
let
    #"Changed Type" = 1,
    Next = #"Changed Type" + 1
in
    Next
```

```text
2
```

A `let` is an expression like any other: it can sit inside another one, and its names are
only visible inside it.

```m
let
    total = let x = 2, y = 3 in x * y
in
    total + 1
```

```text
7
```

A function that calls itself from inside the `let` that defines it needs `@` in front of its
own name.

```m
let
    Fact = (n) => if n <= 1 then 1 else n * @Fact(n - 1)
in
    Fact(5)
```

```text
120
```

Without the `@`, the name is not in scope inside its own definition.

```m
let
    Fact = (n) => if n <= 1 then 1 else n * Fact(n - 1)
in
    Fact(5)
```

```text
error: Expression.Error: [2,45-2,49] The name 'Fact' doesn't exist in the current context. | Detail: {[Location = [Kind = "Language.TextSourceLocation", Text = "", Range = [Start = [Line = 1, Column = 44], End = [Line = 1, Column = 48]]], Text = "The name 'Fact' doesn't exist in the current context."]}
```
