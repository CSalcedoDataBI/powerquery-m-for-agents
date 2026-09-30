# Review PBIPs

One Power BI project per example category, to read the executed examples in Power BI instead
of in Markdown. The example pages stay the source of truth; these projects are generated from
them.

| Batch | Project |
|---|---|
| Number.Operations | [number-operations/NumberOperations.pbip](number-operations/NumberOperations.pbip) |
| Number.Conversion and formatting | [number-conversion-and-formatting/NumberConversionAndFormatting.pbip](number-conversion-and-formatting/NumberConversionAndFormatting.pbip) |

## How to review

1. Open the `.pbip` in Power BI Desktop and click **Refresh**.
2. The **Examples** page lists every block: the function, the code, **Recorded** (the result its
   page shows) and **Live** (what your Power BI returns now). **Match** is `yes` when they agree.
   Filter by function with the slicer on the left.
3. A `NO` in Match means the page and the engine disagree: rerun
   `python lab/runner/run_examples.py --port <port> --write` and read the diff.

The last page, **Thank You!!**, is the author's page (`thank-you/`, copied from the Deneb labs).

## How it works

Refresh evaluates every block the way `lab/runner/` does - `runner.pq` renders each value,
over only the members of `#shared` that `m_blocks.allowed_names` allows. No data source: the
examples compute on literals, so the projects need no credentials and read nothing.

```bash
python lab/review/build_review.py --only number-   # add or rebuild a batch
python lab/review/build_review.py                  # rebuild every batch in this folder
python lab/review/build_review.py --check          # CI: exit 1 if a batch is out of date
```
