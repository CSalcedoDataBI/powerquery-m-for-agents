# Evals

## Invented-name A/B (`hallucination/`)

Does the reference stop an agent from writing M library names that do not exist? Each
question in [`questions.yaml`](hallucination/questions.yaml) is answered twice by the same
model: once alone (arm A), and once with the catalogue rows of its category (arm B: names
and one-line summaries, never the card that holds the answer).

In the code of every answer, each dotted name (`Table.AddColumn`, `BinaryFormat.Byte`) and
each `#` literal is looked up in `skills/m-reference/generated/catalog/`. A name the export
does not have is an invention. No model judges another: the count is a lookup, and it can be
re-run on a saved answer file at no cost.

The bank has two regimes, never averaged together: `core` (Text, List, Table, Record,
Number, dates) and `deep` (BinaryFormat, Splitter, Combiner, Replacer, Comparer, Type,
Expression, Lines, Uri, Cube, Diagnostics, Function, metadata).

```bash
python evals/hallucination/run_ab.py --model claude-haiku-4-5-20251001 --out run.json
python evals/hallucination/run_ab.py --replay evals/hallucination/runs/<file>.json
python -m unittest discover -s evals/hallucination -t evals/hallucination
```

It calls the Anthropic or DeepSeek API, with `ANTHROPIC_API_KEY` or `DEEPSEEK_API_KEY` read
from the environment (never from the command line, never written to the run file). The run
files in [`hallucination/runs/`](hallucination/runs/) keep every answer, so every number can
be re-counted with `--replay`.

Known limit: the catalogue is one host, Power BI Desktop. A name that exists only in another
host would count as invented; the system prompt says Power BI Desktop for that reason (#2).
