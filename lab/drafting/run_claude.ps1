<#
.SYNOPSIS
  Answers each prompt of a pilot run with a Claude-quality model, through a reviewer CLI
  that speaks the second-opinion interface (-p / --prompt-file / -o / --gasto).

.DESCRIPTION
  The drafting alternative to run_dsh.ps1 (#21): instead of a local DeepSeek container, each
  prompt is answered by the Anthropic API behind a CLI that already owns the key and the
  spend plumbing. Nothing changes downstream - pilot.py collect still decides what, if
  anything, reaches skills/, and the lab runner still writes every result.

  The reviewer is any command with the claude-review / second-opinion interface:
    - `-Reviewer <cmd>` (default `claude-review`, resolved on PATH) answers a prompt with
      `--prompt-file <f> -o <answer>` and reports its running spend with `--gasto`;
    - the API key never touches this repo: the reviewer reads it itself (claude-review takes
      ANTHROPIC_API_KEY_PROMO from Bitwarden Secrets Manager) and never prints it;
    - `-Ceiling <usd>` stops the run before the next call once the reviewer's own spend log
      reaches that total, so a drafting pass cannot overrun a budget.

  Answers land in <Out>/answers/<file>.md and timings in <Out>/runs.json. The model writes
  only the ```m blocks and the note; the same checks as any page (pilot.py collect, then the
  lab runner and check_examples.py) decide what stays. A page already answered is skipped
  unless -Redraft, so a capped or interrupted run resumes where it stopped.

.EXAMPLE
  pwsh lab/drafting/run_claude.ps1 -Out lab/drafting/out/claude -CheckOnly
  pwsh lab/drafting/run_claude.ps1 -Out lab/drafting/out/claude -Only number-acos,number-asin
  pwsh lab/drafting/run_claude.ps1 -Out lab/drafting/out/claude -Ceiling 93
#>
[CmdletBinding(PositionalBinding = $false)]
param(
    [Parameter(Mandatory)][string]$Out,
    [string[]]$Only,
    [string]$Reviewer = 'claude-review',
    [string]$Model = 'claude-opus-5-5',
    [double]$Ceiling = 0,
    [switch]$Redraft,
    [switch]$CheckOnly
)
$ErrorActionPreference = 'Stop'
$Out = (Resolve-Path $Out).Path
$prompts = Join-Path $Out 'prompts'
$answers = Join-Path $Out 'answers'
if (-not (Test-Path $prompts)) { throw "No prompts in $prompts - run: python lab/drafting/pilot.py prompts --out $Out" }
New-Item -ItemType Directory -Force $answers | Out-Null

if (-not (Get-Command $Reviewer -ErrorAction SilentlyContinue)) {
    throw "reviewer CLI '$Reviewer' not found on PATH (needs the claude-review / second-opinion interface)"
}

function Get-Spend {
    # The reviewer's own spend log: "... US$<n> de US$200 ...". $null if it reports none.
    $line = (& $Reviewer --gasto 2>&1) -join "`n"
    if ($line -match 'US\$([0-9]+(?:\.[0-9]+)?)\s+de') { return [double]$Matches[1] }
    return $null
}

$files = Get-ChildItem $prompts -Filter *.txt | Sort-Object Name
if ($Only) { $wanted = $Only -split ','; $files = $files | Where-Object { $_.BaseName -in $wanted } }
if (-not $Redraft) {
    $files = $files | Where-Object {
        $a = Join-Path $answers "$($_.BaseName).md"
        -not ((Test-Path $a) -and (Get-Item $a).Length -gt 0)
    }
}

$start = Get-Spend
Write-Host ("Reviewer $Reviewer ($Model). {0} prompt(s) to answer. Spend so far: {1}." -f `
        @($files).Count, $(if ($null -ne $start) { "US`$$start" } else { 'unknown' }))
if ($Ceiling -gt 0) { Write-Host "Stopping once logged spend reaches US`$$Ceiling (checked before each call)." }
if ($CheckOnly) { $files | ForEach-Object { "  would draft $($_.BaseName)" }; return }

$runs = @()
foreach ($f in $files) {
    if ($Ceiling -gt 0) {
        $now = Get-Spend
        # Fail closed: an unreadable spend log with a ceiling set would otherwise draft with no cap.
        if ($null -eq $now) {
            throw "cannot read spend from '$Reviewer --gasto'; refusing to draft with -Ceiling set (the budget guard would fail open)"
        }
        if ($now -ge $Ceiling) {
            Write-Warning "Spend US`$$now reached the ceiling US`$$Ceiling - stopping; run again to resume."
            break
        }
    }
    $target = Join-Path $answers "$($f.BaseName).md"
    $clock = [Diagnostics.Stopwatch]::StartNew()
    & $Reviewer --prompt-file $f.FullName --model $Model -o $target 2>&1 | Out-Null
    $exit = $LASTEXITCODE
    $clock.Stop()
    # A failed call must leave no answer: a partial or error file would be skipped as "done" on resume.
    if ($exit -ne 0 -and (Test-Path $target)) { Remove-Item $target }
    $runs += [ordered]@{ file = $f.BaseName; exit = $exit; seconds = [math]::Round($clock.Elapsed.TotalSeconds, 1) }
    Write-Host ("  {0,-30} exit {1}  {2,6:n1}s" -f $f.BaseName, $exit, $clock.Elapsed.TotalSeconds)
}
# Merge with earlier passes (resume keeps their timings); a later pass's entry wins per file.
$runsPath = Join-Path $Out 'runs.json'
$merged = [ordered]@{}
if (Test-Path $runsPath) { foreach ($r in @(Get-Content $runsPath -Raw | ConvertFrom-Json)) { if ($r.file) { $merged[$r.file] = $r } } }
foreach ($r in $runs) { $merged[$r.file] = $r }
$merged.Values | ConvertTo-Json -AsArray | Set-Content $runsPath -Encoding utf8
$end = Get-Spend
if ($null -ne $start -and $null -ne $end) { Write-Host ("Spend this pass: US`${0:n2} (US`${1} -> US`${2})." -f ($end - $start), $start, $end) }
