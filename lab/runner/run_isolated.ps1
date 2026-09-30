<#
.SYNOPSIS
  Evaluates each case of lab/runner in its own refresh of an already-open Desktop.

.DESCRIPTION
  run_examples.py writes one runner query per case under -CasesDir. For each file this script
  copies it over runner-query.pq (the file the model's partition reads), refreshes the table and
  reads its row, so no two cases share an evaluation. Evaluated together, cases were seen to
  leak into each other: a table type from one case showed up in another (2026-09-29).

  Windows PowerShell 5.1 (powershell.exe): the ADOMD client Desktop ships is .NET Framework.
#>
param(
    [Parameter(Mandatory)] [int]$Port,
    [Parameter(Mandatory)] [string]$CasesDir,
    [Parameter(Mandatory)] [string]$QueryFile,
    [Parameter(Mandatory)] [string]$OutFile,
    [string]$Table = "ExamplesRunner",
    [string]$DesktopExe = "$env:ProgramFiles\Microsoft Power BI Desktop\bin\PBIDesktop.exe"
)
$ErrorActionPreference = "Stop"
Add-Type -Path (Join-Path (Split-Path $DesktopExe) "Microsoft.PowerBI.AdomdClient.dll")

$conn = New-Object Microsoft.AnalysisServices.AdomdClient.AdomdConnection("Data Source=localhost:$Port")
$conn.Open()
$cmd = $conn.CreateCommand()
$refresh = '{ "refresh": { "type": "full", "objects": [{ "database": "' + $conn.Database + '", "table": "' + $Table + '" }] } }'
$utf8 = New-Object Text.UTF8Encoding($false)

$rows = New-Object System.Collections.ArrayList
$files = @(Get-ChildItem $CasesDir -Filter *.pq | Sort-Object Name)
$sw = [Diagnostics.Stopwatch]::StartNew()
foreach ($f in $files) {
    [IO.File]::WriteAllText($QueryFile, [IO.File]::ReadAllText($f.FullName, $utf8), $utf8)
    $cmd.CommandText = $refresh
    [void]$cmd.ExecuteNonQuery()
    $cmd.CommandText = "EVALUATE '$Table'"
    $r = $cmd.ExecuteReader()
    while ($r.Read()) {
        [void]$rows.Add([ordered]@{ seq = [int64]$r.GetValue(0); id = [string]$r.GetValue(1); result = [string]$r.GetValue(2) })
    }
    $r.Close()
}
$conn.Close()
[IO.File]::WriteAllText($OutFile, (ConvertTo-Json -InputObject @($rows) -Depth 3 -Compress), $utf8)
Write-Output ("{0} case(s), each in its own refresh, in {1:N0} s." -f $files.Count, $sw.Elapsed.TotalSeconds)
