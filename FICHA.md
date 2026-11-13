# Ficha — powerquery-m-for-agents

> The north of this tool. Its experto (`.claude/agents/experto.md`) reads it on every pull
> request and merges against it. Maintained with the maintainer's internal rules.
> Changing this file requires a new approval: the commit that changes it must also touch the
> `Approved:` line.

## What it is

- **What it builds and for whom:** a Claude Code plugin that gives AI agents the Power Query M
  language as the engine itself reports it: one card per library function (signature, types,
  return, hosts) generated from a `#shared` export, constants, language concept pages, executed
  examples and field notes measured in a lab. Its users are agents writing or reviewing M for
  Power BI Desktop, Excel and Dataflows Gen2, and the people who install the plugin.
- **Role:** tool (a reference plugin; the plugin runs nothing, it is Markdown that Claude reads).
- **Public/private twin:** has a private twin for working material (raw exports and review
  PBIPs), which this repository never names in what an agent reads.

## North

- **Current plan:** the open issues of this repository. Today: second host (#2), the planned
  skills `m-folding` (#8), `m-custom-functions` (#9) and `m-iteration` (#10), CI parity with
  `dax-for-agents` (#12), directory readiness (#35) and the field notes filed by consumers
  (#64, #66, #67, #71, #72).
- **Its measure of success:** fewer invented M names. The table in the README is recounted in
  CI from the saved runs (`scripts/check_eval_claims.py`); a change that makes the reference
  bigger but not more trustworthy is off the north.
- **What this tool is NOT:**
  - not data modeling, partitions, TMDL or incremental refresh policy (the README points to
    the skills that cover those);
  - not DAX (that is `dax-for-agents`);
  - not custom connector development;
  - not a place for function names that did not come from a `#shared` export: it exists to
    stop invention and cannot contain any;
  - not a runtime: the plugin ships no hooks, agents, MCP or LSP servers, and sends nothing
    except the issue `m-feedback` files after the user approves its text.

## Protected zones

What is not touched without an issue that names it:

- `plugins/powerquery-m-for-agents/` — the only folder that ships and the path the plugin
  directory listing was submitted with; it cannot be moved from the portal. It stays under
  512 files (`scripts/validate_skills.py` fails the build at that count) and holds only what
  the skills read at run time.
- `plugins/powerquery-m-for-agents/skills/m-reference/generated/` and `catalog/` — written only
  by `scripts/sync_shared.py` from an export. A card is never edited by hand; a correction is a
  note in `notes/`.
- The `stable` branch — the plugin directory reviews every commit that reaches it. It moves
  only to the commit of a published release, fast-forward and never forced
  (`.github/workflows/stable.yml` and the release step of `release-please.yml`).
- `.gitattributes` — every line-ending rule carries `eol=lf`, with no `export-ignore`,
  `export-subst` or content filter: the directory refused the repository once for each.
- Skill names (`m-reference`, `m-feedback`, the `m-` prefix) and the plugin name — users invoke
  them as `powerquery-m-for-agents:<skill>`; renaming one breaks every install.
- `evals/hallucination/runs/` and the invention table of the README — the table is a claim
  checked against those saved runs; a run is added, never rewritten.
- `plugins/powerquery-m-for-agents/PRIVACY.md` and the README section «What it runs, sends and
  downloads» — they are what the directory listing declares; changing what the plugin sends
  changes both, in the same pull request.
- Licensing of texts (`docs/decisions/2026-10-01-textos-con-licencia.md`) — cards quote only
  the MIT one-line descriptions; the engine's long descriptions and examples are not quoted.

## Layer and feedback

- **Node layer:** none. It is a reference that the ETL layer reads when it writes M.
- **Feedback skill:** `powerquery-m-for-agents:m-feedback` (a sanitized issue on this public
  repository, filed only after the user approves the text).

## Check and experto

- **Required CI check:** `validate` (job of `.github/workflows/validate-skills.yml`), in the
  ruleset `main protegida` of `main`.
- **Test suite:** `pip install pyyaml`, then the steps of that job, of which the unit tests are
  `python -m unittest discover -s scripts -t scripts -v` and
  `python -m unittest discover -s evals/hallucination -t evals/hallucination -v`.
- **Runner:** GitHub (public repo).
- **Tag format:** `vX.Y.Z` (existing `v0.1.0`, `v0.2.0`); release-please decides the number.
- **Experto:** `.claude/agents/experto.md`
- **Directory plugin?:** yes. The listing tracks `stable`. Merging into `main` is not
  publishing; `stable` is not touched outside a published release, and merging the
  release-please pull request publishes a new version to the directory, so it waits for the
  maintainer's OK.
- **Visible parts the maintainer approves:** the directory listing and each release that
  reaches it.

## Approval

Approved by the parent by delegation: on 2026-11-12 the maintainer asked in chat «crea todos
los expertos faltantes, revisar que se hagan bien» (create every missing experto and check
that each one is done well).

Approved: 2026-11-12 (parent, by delegation)
