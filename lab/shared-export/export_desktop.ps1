<#
.SYNOPSIS
  Runs export_shared.pq inside Power BI Desktop and writes exports/<host>-<version>.json.

.DESCRIPTION
  Opens SharedExport.pbip (build it first with build_pbip.py), waits for Desktop's local
  Analysis Services engine, refreshes the one table over TMSL, reads the JSON chunks back
  with a DAX query and saves them as the chunk table sync_shared.py accepts.

  Any other one-table PBIP works the same way: -Pbip, -Table, -OrderBy and -OutFile point
  it elsewhere, and every row is written as an object keyed by column name. lab/runner uses
  that to execute the examples.

  Uses the ADOMD client Desktop ships in its own bin folder, so nothing is downloaded.
  Those assemblies are .NET Framework: run with Windows PowerShell 5.1 (powershell.exe),
  not pwsh.

.EXAMPLE
  powershell.exe -ExecutionPolicy Bypass -File lab/shared-export/export_desktop.ps1
#>
param(
    [string]$DesktopExe = "$env:ProgramFiles\Microsoft Power BI Desktop\bin\PBIDesktop.exe",
    [string]$HostName = "desktop",
    [int]$TimeoutSeconds = 300,
    [string]$Pbip = "",
    [string]$Table = "SharedExport",
    [string]$OrderBy = "part",
    [string]$OutFile = "",
    # Close the Desktop this script opened once the rows are saved (it never saves the file).
    [switch]$Close,
    # Read from a Desktop that is already open on this port instead of starting one, so one
    # instance serves every run. -NoRefresh skips the refresh when something else (the
    # powerbi-modeling MCP) already refreshed the table.
    [int]$Port = 0,
    [switch]$NoRefresh
)
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = Resolve-Path (Join-Path $here "..\..")
$pbip = if ($Pbip) { $Pbip } else { Join-Path $here "SharedExport.pbip" }
if (-not $Port -and -not (Test-Path $pbip)) { throw "Missing $pbip - build it first (build_pbip.py or lab/runner)." }

$version = (Get-Item $DesktopExe).VersionInfo.FileVersion
Add-Type -Path (Join-Path (Split-Path $DesktopExe) "Microsoft.PowerBI.AdomdClient.dll")

if ($Port) {
    $port = $Port
    $desktop = $null
    $conn = New-Object Microsoft.AnalysisServices.AdomdClient.AdomdConnection("Data Source=localhost:$port")
    $conn.Open()
} else {
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
                "Usually the partition's M does not parse, or the PBIP is stale: rebuild it " +
                "(build_pbip.py --check tells for SharedExport). Desktop is left open " +
                "(PID $($desktop.Id)) so you can read the message.")
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
            if ($names -contains $Table) { $conn = $c } else { $c.Close() }
        } catch { }
    }
}
$db = $conn.Database
$cmd = $conn.CreateCommand()
if ($NoRefresh) {
    Write-Output "Engine on localhost:$port. Reading $Table as it is (no refresh)..."
} else {
    Write-Output "Engine on localhost:$port. Refreshing $Table..."
    $cmd.CommandText = '{ "refresh": { "type": "full", "objects": [{ "database": "' + $db + '", "table": "' + $Table + '" }] } }'
    $sw = [Diagnostics.Stopwatch]::StartNew()
    [void]$cmd.ExecuteNonQuery()
    Write-Output ("Refreshed in {0:N1} s." -f $sw.Elapsed.TotalSeconds)
}

$cmd.CommandText = "EVALUATE '$Table' ORDER BY '$Table'[$OrderBy]"
$r = $cmd.ExecuteReader()
# DAX names result columns 'Table'[column]; keep only the column.
$columns = @(0..($r.FieldCount - 1) | ForEach-Object { $r.GetName($_) -replace '^.*\[(.*)\]$', '$1' })
$rows = New-Object System.Collections.ArrayList
while ($r.Read()) {
    $row = [ordered]@{}
    for ($i = 0; $i -lt $columns.Count; $i++) {
        $v = $r.GetValue($i)
        $row[$columns[$i]] = if ($v -is [DBNull]) { $null } else { $v }
    }
    [void]$rows.Add($row)
}
$r.Close(); $conn.Close()
if ($rows.Count -eq 0) { throw "The table came back empty." }

$out = if ($OutFile) { $OutFile } else { Join-Path (Join-Path $root "exports") "$HostName-$version.json" }
$text = ConvertTo-Json -InputObject @($rows) -Depth 3 -Compress
[IO.File]::WriteAllText($out, $text, (New-Object Text.UTF8Encoding($false)))
Write-Output "Wrote $($rows.Count) row(s) to $out"
if (-not $desktop) {
    Write-Output "Desktop on port $port left as it was."
} elseif ($Close) {
    Stop-Process -Id $desktop.Id -Force -ErrorAction SilentlyContinue
    Write-Output "Closed the Desktop this script opened (PID $($desktop.Id)); nothing was saved."
} else {
    Write-Output "Desktop left open (PID $($desktop.Id)); close it without saving."
}
