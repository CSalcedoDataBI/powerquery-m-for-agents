<#
.SYNOPSIS
  Answers each prompt of a pilot run with dsh, one throwaway container per function (#21).

.DESCRIPTION
  The container gets no host path and exactly one secret:
    - the prompt goes in on stdin and the answer comes out on stdout (dsh --json);
    - DEEPSEEK_API_KEY is read from the Windows user registry into this process and handed to
      docker by NAME (-e DEEPSEEK_API_KEY), so the value is never on a command line;
    - before any model call, the container's environment is listed (names only) and the run
      stops if anything but the expected names is there;
    - read-only root, tmpfs home and work dir, all capabilities dropped, no new privileges,
      no published port (headless opens none);
    - the privacy patch baked into the image turns off the session-log and plugin-inventory
      uploads, and DSH_TELEMETRY_DISABLED turns off telemetry export. Before the real key is
      even read, a container with no network and a fake key runs one whole turn against a
      stand-in API on its own loopback (capture.mjs), and the run stops if the turn does not
      complete or if either field appears anywhere in any request.
  Answers land in <Out>/answers/<file>.jsonl and timings in <Out>/runs.json; pilot.py
  collect decides what, if anything, reaches skills/.

.EXAMPLE
  pwsh lab/drafting/run_dsh.ps1 -Out lab/drafting/out/dsh -CheckOnly   # build + all checks, no model call
  pwsh lab/drafting/run_dsh.ps1 -Out lab/drafting/out/dsh -Only number-mod,number-abs
  pwsh lab/drafting/run_dsh.ps1 -Out lab/drafting/out/dsh
#>
[CmdletBinding(PositionalBinding = $false)]
param(
    [Parameter(Mandatory)][string]$Out,
    [string]$Image = 'pq-drafting-dsh:0.2.0-rc.2',
    [string[]]$Only,
    [switch]$CheckOnly,
    [int]$TimeoutSec = 600
)
$ErrorActionPreference = 'Stop'
$Out = (Resolve-Path $Out).Path
$prompts = Join-Path $Out 'prompts'
$answers = Join-Path $Out 'answers'
if (-not (Test-Path $prompts)) { throw "No prompts in $prompts - run: python lab/drafting/pilot.py prompts --out $Out" }
New-Item -ItemType Directory -Force $answers | Out-Null

# Always built from this folder, and run by the image ID of what was just built: an image that
# merely carries the tag - stale, or put there by something else - never receives the key.
# `docker build -q` prints the digest of an index (image + attestation) that docker may clean
# up mid-run ("No such image"), so the ID is read back from the tag the build just set.
$buildLog = docker build -q -t $Image $PSScriptRoot 2>&1
if ($LASTEXITCODE -ne 0) { throw "docker build failed:`n$($buildLog -join "`n")" }
$Image = docker image inspect --format '{{.Id}}' $Image
if ($LASTEXITCODE -ne 0 -or $Image -notmatch '^sha256:[0-9a-f]{64}$') { throw "could not read the built image ID: $Image" }

# /tmp alone is exec: dsh's native-addon loader copies its prebuilt .node there before loading
# it, and docker mounts tmpfs noexec by default ("failed to map segment from shared object").
$sandbox = @('--rm', '--read-only', '--tmpfs', '/tmp:exec',
    '--tmpfs', '/home/node:uid=1000,gid=1000', '--tmpfs', '/work:uid=1000,gid=1000',
    '--cap-drop', 'ALL', '--security-opt', 'no-new-privileges',
    '--pids-limit', '256', '--memory', '2g', '--cpus', '2')

# Privacy check: no network, a fake key, the API replaced by capture.mjs on the loopback. The
# stand-in answers successfully, so dsh runs a whole turn and every request of it is checked.
$capture = 'node /cfg/capture.mjs & sleep 1; echo "Say ok." | ' +
    'DEEPSEEK_BASE_URL=http://127.0.0.1:8799 DEEPSEEK_API_KEY=sk-fake-privacy-check ' +
    'dsh-run --profile headless --json > /tmp/out.jsonl 2>&1 && ' +
    'grep -q ''"reason":{"kind":"completed"}'' /tmp/out.jsonl && echo TURN-COMPLETED; ' +
    'cat /tmp/request-fields.txt'
$probeOut = docker run @sandbox --network none --entrypoint sh $Image -c $capture
if ($LASTEXITCODE -ne 0) { throw 'Privacy check: the probe container failed' }
if ('TURN-COMPLETED' -notin $probeOut) { throw 'Privacy check: dsh did not complete a turn against the stand-in API' }
$sent = @($probeOut | Where-Object { $_ -like 'POST *' })
if (-not $sent) { throw 'Privacy check: dsh sent no request to the stand-in API' }
$leaks = $sent | Select-String -Pattern 'LEAK|UNREADABLE|dsh_session_log|dsh_plugin_packages'
if ($leaks) { throw "Privacy check failed - still sent:`n$($leaks -join "`n")" }
Write-Host "Privacy check: $(@($sent).Count) request(s), fields: $((@($sent)[0] -split ' ')[2])"

# The same container, without network and with a fake key, is what every check inspects:
# the real key reaches only the containers that answer a prompt.
$probe = $sandbox + @('--network', 'none', '-e', 'DEEPSEEK_API_KEY=sk-fake-probe')
# What the image, docker and sh (PWD) put there, plus the one secret. Anything else stops the run.
$allowed = 'PATH', 'HOSTNAME', 'HOME', 'NODE_VERSION', 'YARN_VERSION', 'DSH_TELEMETRY_DISABLED',
    'NO_UPDATE_NOTIFIER', 'NPM_CONFIG_UPDATE_NOTIFIER', 'DSH_HOME', 'PWD', 'DEEPSEEK_API_KEY'
$names = docker run @probe --entrypoint sh $Image -c 'env | cut -d= -f1' |
    Where-Object { $_ } | Sort-Object
if ($LASTEXITCODE -ne 0) { throw 'could not list the container environment' }
Write-Host "Container environment: $($names -join ', ')"
$extra = $names | Where-Object { $_ -notin $allowed }
if ($extra) { throw "Unexpected variables in the container: $($extra -join ', ')" }
# Kernel filesystems, the tmpfs above, and the three files docker itself mounts - those only
# as docker mounts them (ext4, read-only): a host file bind-mounted over one would not be.
$mounts = docker run @probe --entrypoint sh $Image -c 'awk ''$3 !~ /^(proc|sysfs|tmpfs|devpts|mqueue|cgroup2?|overlay)$/ && !($2 ~ /^\/etc\/(hostname|hosts|resolv\.conf)$/ && $3 == "ext4" && $4 ~ /^ro,/)'' /proc/mounts'
if ($LASTEXITCODE -ne 0) { throw 'could not read the container mounts' }
if ($mounts) { throw "Unexpected mounts in the container:`n$($mounts -join "`n")" }
$version = docker run @probe $Image --version
if ($LASTEXITCODE -ne 0) { throw 'dsh --version failed in the container' }
Write-Host "dsh $version - isolation checked (no host mount, one secret)."
if ($CheckOnly) { return }

$key = [Environment]::GetEnvironmentVariable('DEEPSEEK_API_KEY', 'User')
if (-not $key) { throw 'DEEPSEEK_API_KEY is not set in the user registry.' }
$env:DEEPSEEK_API_KEY = $key
Remove-Variable key
$isolation = $sandbox + @('-e', 'DEEPSEEK_API_KEY')

try {
    $files = Get-ChildItem $prompts -Filter *.txt | Sort-Object Name
    # -Only a,b,c arrives as one string through pwsh -File.
    if ($Only) { $wanted = $Only -split ','; $files = $files | Where-Object { $_.BaseName -in $wanted } }
    $runs = @()
    foreach ($f in $files) {
        $target = Join-Path $answers "$($f.BaseName).jsonl"
        $errors = Join-Path $answers "$($f.BaseName).stderr.txt"
        $name = "pq-dsh-$($f.BaseName)-$PID"
        $argv = @('run', '-i', '--name', $name) + $isolation +
            @($Image, '--profile', 'headless', '--json')
        $clock = [Diagnostics.Stopwatch]::StartNew()
        $p = Start-Process docker -ArgumentList $argv -NoNewWindow -PassThru `
            -RedirectStandardInput $f.FullName -RedirectStandardOutput $target -RedirectStandardError $errors
        if (-not $p.WaitForExit($TimeoutSec * 1000)) {
            docker kill $name *> $null
            $p.WaitForExit()
        }
        $clock.Stop()
        # Nothing should ever print the key; if a crash dump or a debug line did, it does not
        # stay on disk.
        foreach ($written in $target, $errors) {
            $text = Get-Content $written -Raw -ErrorAction SilentlyContinue
            if ($text -and $text.Contains($env:DEEPSEEK_API_KEY)) {
                Set-Content $written $text.Replace($env:DEEPSEEK_API_KEY, '[REDACTED]') -NoNewline -Encoding utf8
                Write-Warning "The key appeared in $(Split-Path $written -Leaf) and was redacted."
            }
        }
        $runs += [ordered]@{ file = $f.BaseName; exit = $p.ExitCode; seconds = [math]::Round($clock.Elapsed.TotalSeconds, 1) }
        Write-Host ("  {0,-28} exit {1}  {2,6:n1}s" -f $f.BaseName, $p.ExitCode, $clock.Elapsed.TotalSeconds)
    }
    $runs | ConvertTo-Json -AsArray | Set-Content (Join-Path $Out 'runs.json') -Encoding utf8
}
finally {
    Remove-Item Env:DEEPSEEK_API_KEY -ErrorAction SilentlyContinue
}
