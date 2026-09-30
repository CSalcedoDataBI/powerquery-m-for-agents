# Drafting with an outside model

A pilot (issue #21): can a low-cost agent harness draft executed-example pages well enough that
bulk coverage stops costing the main agent's quota? The harness under test is
[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`, MIT, developer
preview), headless profile, its default model `deepseek-flash`.

Nothing the model writes is trusted. It drafts the ```` ```m ```` blocks and one-line notes; the
engine writes every result, and the same checks as any page decide what stays.

```bash
python lab/drafting/pilot.py prompts --out lab/drafting/out/dsh     # one prompt per function
pwsh lab/drafting/run_dsh.ps1 -Out lab/drafting/out/dsh -CheckOnly   # build + isolation check, no model call
pwsh lab/drafting/run_dsh.ps1 -Out lab/drafting/out/dsh              # one container per function
python lab/drafting/pilot.py collect --out lab/drafting/out/dsh     # answers -> examples/
python lab/runner/run_examples.py --port <port> --write --only examples/number-
python scripts/check_examples.py
python lab/drafting/pilot.py report --out lab/drafting/out/dsh
```

`lab/drafting/out/` is ignored by git: prompts, raw answers and timings stay on the machine.

## Isolation

| Rule | How |
|---|---|
| `dsh` never runs on the host | Only in the image built from `Dockerfile` (`node:24-bookworm-slim`, `dsh` pinned) |
| One secret | `DEEPSEEK_API_KEY` from the Windows user registry, passed by name (`-e DEEPSEEK_API_KEY`), never on a command line. Before any model call the container's variables are listed (names only) and the run stops on anything unexpected |
| No host files | No mount at all: the prompt goes in on stdin, the answer comes out on stdout. The run checks `/proc/mounts` and stops on any mount beyond the kernel's, its tmpfs and docker's own `/etc/hosts`-type files |
| Least privilege | Read-only root, tmpfs home and work dir (only `/tmp` allows exec: dsh loads its native addon from there), `--cap-drop ALL`, `no-new-privileges`, memory, CPU and PID limits, no published port (headless opens none) |
| Only what the task needs leaves | `privacy.patch.yml` turns off the two extras `dsh` sends the API by default (the session log and the plugin-package list); `DSH_TELEMETRY_DISABLED` turns off telemetry export. No third-party plugins |
| The runner stays on the host | `dsh` never touches Power BI Desktop |

## What comes back

`pilot.py collect` takes an answer only as far as it is safe:

- a ```` ```text ```` block or a lab stamp in an answer is dropped and counted;
- a block that could reach outside the engine refuses the whole page (`m_blocks.unsafe_calls`,
  the same rule `check_examples.py` applies to every page on CI, and the runner applies before it
  evaluates anything);
- outside ```` ```m ```` blocks a page may hold headings and plain prose only: another fence,
  HTML or a link refuses it;
- a page is written only as `examples/<category>/<file>.md` of a pilot function, never over an
  existing page without `--force`.

None of that judges the prose. **Every page is read by a person before it is committed**, against
the results the engine wrote: in the pilot that review edited 3 of 26 pages (a made-up argument
value, a claim the result contradicted, a mechanism the page could not show).
