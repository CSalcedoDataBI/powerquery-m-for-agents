# Contributing

Repository conventions (language, generated files, how counts are checked) are in
[INDEX.md](INDEX.md#conventions) and [CLAUDE.md](CLAUDE.md). Work lands on `main` through a pull
request; CI (`.github/workflows/validate-skills.yml`) must pass.

## What ships

Only [`plugins/powerquery-m-for-agents/`](plugins/powerquery-m-for-agents/) is the plugin.
Keep it to what the skills read at run time; tools, tests, docs and evals stay outside it.
The plugin directory holds a plugin of 512 files or more for review, and
`scripts/validate_skills.py` fails the build at that count.

## Releases and the plugin directory

The claude.ai plugin directory tracks the **`stable`** branch, not `main`. It scans every
commit that lands on the branch it tracks and puts each one in review, replacing the one
before. `stable` moves only when a release is published, so `main` can take commits every day.
Claude Code users who install from this repo's marketplace still get `main`.

A release is two steps by hand and one automatic:

1. Bump `version` in `plugins/powerquery-m-for-agents/.claude-plugin/plugin.json` on `main`,
   through a pull request.
2. Tag the merged commit and publish the release: `git tag -a vX.Y.Z <sha>`,
   `git push origin vX.Y.Z`, `gh release create vX.Y.Z --verify-tag`.
3. `.github/workflows/stable.yml` then fast-forwards `stable` to that commit. If it fails
   because it is not a fast-forward, stop: never force `stable`.

- **Batch the work.** A release is a review cycle measured in days, not a deploy.
- **Test before releasing**, in Claude Code against the local plugin
  (`claude --plugin-dir plugins/powerquery-m-for-agents`): what is on claude.ai is only ever
  what the reviewer approved.
- **Do not release while a version is in review**, unless it carries a security fix: it
  replaces the version the reviewer is reading.
- Never push to `stable` outside a release, and never force it.
