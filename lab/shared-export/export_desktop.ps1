<#
.SYNOPSIS
  Runs export_shared.pq inside Power BI Desktop and writes exports/<host>-<version>.json.

.DESCRIPTION
  Opens SharedExport.pbip (build it first with build_pbip.py), waits for Desktop's local
  Analysis Services engine, refreshes the one table over TMSL, reads the JSON chunks back
  with a DAX query and saves them as the chunk table sync_shared.py accepts.

  Uses the ADOMD client Desktop ships in its own bin folder, so nothing is downloaded.
  Those assemblies are .NET Framework: run with Windows PowerShell 5.1 (powershell.exe),
  not pwsh.

.EXAMPLE
  powershell.exe -ExecutionPolicy Bypass -File lab/shared-export/export_desktop.ps1
#>
param(
    [string]$DesktopExe = "$env:ProgramFiles\Microsoft Power BI Desktop\bin\PBIDesktop.exe",
    [string]$HostName = "desktop",
    [int]$TimeoutSeconds = 300
)
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = Resolve-Path (Join-Path $here "..\..")
$pbip = Join-Path $here "SharedExport.pbip"
if (-not (Test-Path $pbip)) { throw "Missing $pbip - run build_pbip.py first." }

$version = (Get-Item $DesktopExe).VersionInfo.FileVersion
Add-Type -Path (Join-Path (Split-Path $DesktopExe) "Microsoft.PowerBI.AdomdClient.dll")

# Engines that exist before we open the file are someone else's model: never touch them.
$before = @((Get-Process msmdsrv -ErrorAction SilentlyContinue).Id)
# A model that fails to load (an M parse error, say) never creates a table: the engine port
# listens but TMSCHEMA_TABLES stays empty. Desktop's only trace is a frown snapshot, so a new
# one - or Desktop exiting - ends the wait instead of the timeout.
$frownDir = Join-Path $env:LOCALAPPDATA "Microsoft\Power BI Desktop"
$started = Get-Date
$desktop = Start-Process -FilePath $DesktopExe -ArgumentList "`"$pbip`"" -PassThru
Write-Output "Opened Desktop $version (PID $($desktop.Id)); waiting for its engine..."

function Find-Port {
    foreach ($proc in Get-Process msmdsrv -ErrorAction SilentlyContinue) {
        if ($before -contains $proc.Id) { continue }
        $conn = Get-NetTCPConnection -State Listen -OwningProcess $proc.Id -ErrorAction SilentlyContinue |
            Select-Object -First 1
        if ($conn) { return $conn.LocalPort }
    }
    return $null
}

function Assert-DesktopHealthy {
    if ($desktop.HasExited) {
        throw "Desktop exited (code $($desktop.ExitCode)) before the model loaded."
    }
    $frown = Get-ChildItem $frownDir -Filter "FrownSnapShot*.zip" -ErrorAction SilentlyContinue |
        Where-Object { $_.LastWriteTime -ge $started } |
        Sort-Object LastWriteTime | Select-Object -First 1
    if ($frown) {
        throw ("Desktop reported an error while loading the model (frown snapshot $($frown.FullName)). " +
            "Usually export_shared.pq does not parse, or SharedExport.pbip is stale: run " +
            "build_pbip.py --check. Desktop is left open (PID $($desktop.Id)) so you can read the message.")
    }
}

$deadline = (Get-Date).AddSeconds($TimeoutSeconds)
$conn = $null
while (-not $conn) {
    Assert-DesktopHealthy
    if ((Get-Date) -gt $deadline) { throw "No model came up within $TimeoutSeconds s." }
    Start-Sleep -Seconds 3
    $port = Find-Port
    if (-not $port) { continue }
    try {
        $c = New-Object Microsoft.AnalysisServices.AdomdClient.AdomdConnection("Data Source=localhost:$port")
        $c.Open()
        $cmd = $c.CreateCommand()
        $cmd.CommandText = "SELECT [Name] FROM `$SYSTEM.TMSCHEMA_TABLES"
        $r = $cmd.ExecuteReader(); $names = @(); while ($r.Read()) { $names += $r.GetValue(0) }; $r.Close()
        if ($names -contains "SharedExport") { $conn = $c } else { $c.Close() }
    } catch { }
}
Write-Output "Engine on localhost:$port. Refreshing SharedExport..."

$db = $conn.Database
$cmd = $conn.CreateCommand()
$cmd.CommandText = '{ "refresh": { "type": "full", "objects": [{ "database": "' + $db + '", "table": "SharedExport" }] } }'
$sw = [Diagnostics.Stopwatch]::StartNew()
[void]$cmd.ExecuteNonQuery()
Write-Output ("Refreshed in {0:N1} s." -f $sw.Elapsed.TotalSeconds)

$cmd.CommandText = "EVALUATE 'SharedExport' ORDER BY 'SharedExport'[part]"
$r = $cmd.ExecuteReader()
$chunks = New-Object System.Collections.ArrayList
while ($r.Read()) { [void]$chunks.Add([ordered]@{ part = [int]$r.GetValue(0); json = [string]$r.GetValue(1) }) }
$r.Close(); $conn.Close()
if ($chunks.Count -eq 0) { throw "The table came back empty." }

$outDir = Join-Path $root "exports"
$out = Join-Path $outDir "$HostName-$version.json"
$text = ConvertTo-Json -InputObject @($chunks) -Depth 3 -Compress
[IO.File]::WriteAllText($out, $text, (New-Object Text.UTF8Encoding($false)))
Write-Output "Wrote $($chunks.Count) chunk(s) to $out"
Write-Output "Desktop left open (PID $($desktop.Id)); close it without saving."
