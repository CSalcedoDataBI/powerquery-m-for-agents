# Drafting with an outside model

Bulk coverage of executed-example pages should not cost the main agent's quota, so an outside
model drafts them. Nothing the model writes is trusted: it drafts the ```` ```m ```` blocks and
one-line notes only; the engine writes every result, and the same checks as any page
(`pilot.py collect`, then the lab runner and `check_examples.py`) decide what stays.

The prompt, the collect step and every safety check are shared; only how a prompt is answered
differs. Two harnesses answer it:

- **Claude, through a reviewer CLI** (`run_claude.ps1`) — the current drafter. A command with
  the second-opinion interface (`--prompt-file`, `-o`, `--gasto`, default `claude-review`)
  answers each prompt with the Anthropic API. The CLI owns the key and the spend log, so no key
  reaches this repo and `-Ceiling` caps a pass. A page already answered is skipped, so a capped
  or interrupted pass resumes.
- **DeepSeek, in an isolated container** (`run_dsh.ps1`) — the original pilot (issue #21),
  testing whether a low-cost local harness
  ([DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness), `dsh`, MIT, headless,
  `deepseek-flash`) could do the same with no host access and one secret. Its isolation is below.

```bash
# one prompt per function missing an example, in the given category roots
python lab/drafting/pilot.py prompts --out lab/drafting/out/claude --missing-only --categories Number,Text,Time

# answer each prompt (claude-review, stop once logged spend reaches US$93)
pwsh lab/drafting/run_claude.ps1 -Out lab/drafting/out/claude -Ceiling 93
# ...or the DeepSeek container, one per function (build + isolation check first with -CheckOnly)
pwsh lab/drafting/run_dsh.ps1 -Out lab/drafting/out/dsh

python lab/drafting/pilot.py collect --out lab/drafting/out/claude   # answers -> examples/
python lab/runner/run_examples.py --port <port> --write --only examples/number-
python scripts/check_examples.py
python lab/drafting/pilot.py report --out lab/drafting/out/claude
```

`lab/drafting/out/` is ignored by git: prompts, raw answers and timings stay on the machine.

## Isolation (DeepSeek container)

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
