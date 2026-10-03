# Review PBIPs

One Power BI project per example category, to read the executed examples in Power BI instead
of in Markdown. The example pages stay the source of truth; these projects are generated from
them.

The table on the Examples page shows, for each block, the function's description as the engine
documents it (from its card under `generated/library/`), the code, the result recorded on the
page and the result this Power BI returns after Refresh.

The projects themselves are not in this public repository. They are the maintainer's
working material and live in a private repository, with the raw `#shared` exports; here the
folders are in `.gitignore`, so `build_review.py` writes and checks them in the same place.
What is public is how they are built: `build_review.py` and the `thank-you/` template.

## How to review

1. Open the `.pbip` in Power BI Desktop and click **Refresh**.
2. The **Examples** page lists every block: the function, the code, **Recorded** (the result its
   page shows) and **Live** (what your Power BI returns now). **Match** is `yes` when they agree.
   Filter by function with the slicer on the left.
3. A `NO` in Match means the page and the engine disagree: rerun
   `python lab/runner/run_examples.py --port <port> --write` and read the diff.

The first page, **Thank You!!**, is the author's page and the one each report opens on (`thank-you/`, copied from the Deneb labs). The Examples page comes second.

## How it works

Refresh evaluates every block the way `lab/runner/` does - `runner.pq` renders each value,
over only the members of `#shared` that `m_blocks.allowed_names` allows. No data source: the
examples compute on literals, so the projects need no credentials and read nothing.

```bash
python lab/review/build_review.py --only number-   # add or rebuild a batch
python lab/review/build_review.py                  # rebuild every batch in this folder
python lab/review/build_review.py --check          # exit 1 if a batch is out of date (run locally)
```
