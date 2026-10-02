<#
.SYNOPSIS
  Repeats the column-name casing probe of #20 in an already-open Desktop and records every result.

.DESCRIPTION
  Adds probe tables to the open model (TMSL createOrReplace), refreshes them in fixed groups and
  orders, reads each table, and deletes the probes at the end. Every query is a #table literal or
  parses literal text: no source, no network.

  Each probe returns one row: the column names it sees (Table.ColumnNames), whether
  List.Contains finds "Name" (case-sensitive), and T[Name] read by field access. ProbeLoadC also
  loads its table as is, with model columns Name and Qty, to see what reaches the model.

  Windows PowerShell 5.1 (powershell.exe): the ADOMD client Desktop ships is .NET Framework.

.EXAMPLE
  powershell.exe -NoProfile -File lab/probes/casing_probe.ps1 -Port 51700 -Runs 10 -OutFile casing.json
#>
param(
    [Parameter(Mandatory)] [int]$Port,
    [int]$Runs = 10,
    [Parameter(Mandatory)] [string]$OutFile,
    [string]$DesktopExe = "$env:ProgramFiles\Microsoft Power BI Desktop\bin\PBIDesktop.exe"
)
$ErrorActionPreference = "Stop"
Add-Type -Path (Join-Path (Split-Path $DesktopExe) "Microsoft.PowerBI.AdomdClient.dll")

# What each probe reports about its table T.
$report = 'in #table(type table [cols = text, containsName = text, fieldName = text], {{' +
    'Text.Combine(Table.ColumnNames(T), ","), ' +
    'Text.From(List.Contains(Table.ColumnNames(T), "Name")), ' +
    'try Text.From(T{0}[Name]) otherwise "error"}})'
$probes = [ordered]@{
    # The pair of the original report: same literal shape, names differing only in casing.
    ProbeF   = 'let T = #table(type table [name = text, qty = Int64.Type], {{"z", 9}}) ' + $report
    ProbeC   = 'let T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}}) ' + $report
    # The same names produced by a rename to upper case, not by a literal.
    ProbeU   = 'let T = Table.TransformColumnNames(#table(type table [Name = text, Qty = Int64.Type], {{"q", 5}}), Text.Upper) ' + $report
    # Typed table from parsed text, standing in for a source: no #table literal.
    ProbeS   = 'let T = Table.TransformColumnTypes(Table.PromoteHeaders(Csv.Document("Name,Qty#(lf)a,1#(lf)b,2")), {{"Name", type text}, {"Qty", Int64.Type}}) ' + $report
    ProbeSlc = 'let T = Table.TransformColumnTypes(Table.PromoteHeaders(Csv.Document("name,qty#(lf)z,9")), {{"name", type text}, {"qty", Int64.Type}}) ' + $report
    # Both literals inside one query, the lower-case one evaluated first.
    ProbeSame = 'let F = #table(type table [name = text, qty = Int64.Type], {{"z", 9}}), ' +
        'T = if List.Count(Table.ColumnNames(F)) > 0 then #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}}) else null ' + $report
    # The same, each literal through Expression.Evaluate - how the runner's batch mode evaluates blocks.
    ProbeEval = 'let F = Expression.Evaluate("#table(type table [name = text, qty = Int64.Type], {{""z"", 9}})", #shared), ' +
        'T = if List.Count(Table.ColumnNames(F)) > 0 then Expression.Evaluate("#table(type table [Name = text, Qty = Int64.Type], {{""a"", 1}})", #shared) else null ' + $report
}
$loadC = 'let T = #table(type table [Name = text, Qty = Int64.Type], {{"a", 1}, {"b", 2}, {"a", 3}}) in T'

# Groups refreshed in one TMSL refresh, in the order listed.
$groups = @(
    @('ProbeC'),
    @('ProbeF', 'ProbeC'),
    @('ProbeC', 'ProbeF'),
    @('ProbeU', 'ProbeC'),
    @('ProbeSlc', 'ProbeS'),
    @('ProbeF', 'ProbeS'),
    @('ProbeF', 'ProbeLoadC'),
    @('ProbeSame'),
    @('ProbeEval'),
    @('ProbeF', 'ProbeEval')
)

$conn = New-Object Microsoft.AnalysisServices.AdomdClient.AdomdConnection("Data Source=localhost:$Port")
$conn.Open()
$db = $conn.Database
$cmd = $conn.CreateCommand()

function Invoke-Tmsl([string]$json) { $cmd.CommandText = $json; [void]$cmd.ExecuteNonQuery() }
function Q([string]$s) { ConvertTo-Json $s }

function New-Probe([string]$name, [string]$expr, [string[]]$columns) {
    $cols = ($columns | ForEach-Object {
        $type = if ($_ -eq 'Qty') { 'int64' } else { 'string' }
        '{ "name": ' + (Q $_) + ', "dataType": "' + $type + '", "sourceColumn": ' + (Q $_) + ' }' }) -join ', '
    Invoke-Tmsl ('{ "createOrReplace": { "object": { "database": ' + (Q $db) + ', "table": ' + (Q $name) +
        ' }, "table": { "name": ' + (Q $name) + ', "columns": [' + $cols + '], "partitions": [ { "name": ' +
        (Q $name) + ', "mode": "import", "source": { "type": "m", "expression": ' + (Q $expr) + ' } } ] } } }')
}

$all = @($probes.Keys) + @('ProbeLoadC')
try {
    foreach ($name in $probes.Keys) { New-Probe $name $probes[$name] @('cols', 'containsName', 'fieldName') }
    New-Probe 'ProbeLoadC' $loadC @('Name', 'Qty')

    $rows = New-Object System.Collections.ArrayList
    for ($run = 1; $run -le $Runs; $run++) {
        foreach ($group in $groups) {
            $objects = ($group | ForEach-Object { '{ "database": ' + (Q $db) + ', "table": ' + (Q $_) + ' }' }) -join ', '
            $err = $null
            try { Invoke-Tmsl ('{ "refresh": { "type": "full", "objects": [' + $objects + '] } }') }
            catch { $err = $_.Exception.Message }
            foreach ($name in $group) {
                $row = [ordered]@{ run = $run; group = ($group -join '+'); table = $name; refreshError = $err }
                if (-not $err) {
                    $cmd.CommandText = "EVALUATE '$name'"
                    $r = $cmd.ExecuteReader()
                    $values = @()
                    while ($r.Read()) {
                        $fields = @(); for ($i = 0; $i -lt $r.FieldCount; $i++) { $fields += ($r.GetName($i) + '=' + [string]$r.GetValue($i)) }
                        $values += ($fields -join '; ')
                    }
                    $r.Close()
                    $row.values = $values
                }
                [void]$rows.Add($row)
            }
        }
    }
    $utf8 = New-Object Text.UTF8Encoding($false)
    [IO.File]::WriteAllText($OutFile, (ConvertTo-Json -InputObject @($rows) -Depth 4), $utf8)
    Write-Output ("{0} run(s) x {1} group(s): {2} row(s) to {3}" -f $Runs, $groups.Count, $rows.Count, $OutFile)
}
finally {
    foreach ($name in $all) {
        try { Invoke-Tmsl ('{ "delete": { "object": { "database": ' + (Q $db) + ', "table": ' + (Q $name) + ' } } }') } catch { }
    }
    $conn.Close()
}
