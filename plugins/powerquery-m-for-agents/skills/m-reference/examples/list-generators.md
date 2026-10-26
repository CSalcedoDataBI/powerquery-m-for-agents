<!-- lab: desktop 2.157.879.0 -->

# Executed examples: list-generators

One `## <Name>` section per function. Every ```text block is what the engine returned, written by the lab runner, never typed.

## List.Dates

Three days from a leap day's eve.

```m
List.Dates(#date(2024, 2, 28), 3, #duration(1, 0, 0, 0))
```

```text
{#date(2024, 2, 28), #date(2024, 2, 29), #date(2024, 3, 1)}
```

## List.DateTimes

Hourly steps cross midnight.

```m
List.DateTimes(#datetime(2024, 1, 1, 23, 0, 0), 3, #duration(0, 1, 0, 0))
```

```text
{#datetime(2024, 1, 1, 23, 0, 0), #datetime(2024, 1, 2, 0, 0, 0), #datetime(2024, 1, 2, 1, 0, 0)}
```

## List.DateTimeZones

The offset is kept on every item.

```m
List.DateTimeZones(#datetimezone(2024, 1, 1, 0, 0, 0, -5, 0), 2, #duration(0, 12, 0, 0))
```

```text
{#datetimezone(2024, 1, 1, 0, 0, 0, -5, 0), #datetimezone(2024, 1, 1, 12, 0, 0, -5, 0)}
```

## List.Durations

Half-hour steps.

```m
List.Durations(#duration(0, 0, 0, 0), 3, #duration(0, 0, 30, 0))
```

```text
{#duration(0, 0, 0, 0), #duration(0, 0, 30, 0), #duration(0, 1, 0, 0)}
```

## List.Generate

Powers of two up to 16.

```m
List.Generate(() => 1, each _ <= 16, each _ * 2)
```

```text
{1, 2, 4, 8, 16}
```

## List.Numbers

Four numbers from 0 in steps of 0.5.

```m
List.Numbers(0, 4, 0.5)
```

```text
{0, 0.5, 1, 1.5}
```

## List.Random

With a seed the sequence repeats; its count is the argument.

```m
List.Count(List.Random(3, 42))
```

```text
3
```

## List.Times

Hourly steps from 23:00.

```m
List.Times(#time(23, 0, 0), 3, #duration(0, 1, 0, 0))
```

```text
{#time(23, 0, 0), #time(0, 0, 0), #time(1, 0, 0)}
```
