#!/usr/bin/env python3
"""Build SharedExport.pbip: a one-table model whose partition IS export_shared.pq.

The query is embedded, not copied by hand, so the file that runs in Desktop is always the
one in skills/m-reference/scripts/. Rebuild after editing the query:

  python lab/shared-export/build_pbip.py --host desktop --host-version 2.157.879.0

Then open SharedExport.pbip in Power BI Desktop and run export_desktop.ps1, which refreshes
the table over the local Analysis Services port and writes exports/<host>-<version>.json.

CI runs `build_pbip.py --check`: it rebuilds in memory with the Host and HostVersion the
committed partition already carries and fails if any file on disk differs, so an edit to
export_shared.pq that was never rebuilt cannot leave Desktop exporting the old query.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
QUERY = os.path.join(ROOT, "skills", "m-reference", "scripts", "export_shared.pq")
NAME = "SharedExport"
TABLE = os.path.join(HERE, f"{NAME}.SemanticModel", "definition", "tables", f"{NAME}.tmdl")

# Every file build() produces, keyed by path relative to HERE. build() fills it; main()
# either flushes it to disk or compares it with disk.
FILES = {}


def flush():
    for rel, text in FILES.items():
        path = os.path.join(HERE, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\r\n") as f:
            f.write(text)


def stale_files():
    """Paths whose content on disk differs from the build, ignoring line endings.

    .gitattributes pins CRLF only for TMDL/PBIP/PBIR, so the JSON files check out as LF on
    Linux; the check is about content, not about how git chose to end the lines.
    """
    stale = []
    for rel, text in sorted(FILES.items()):
        path = os.path.join(HERE, rel)
        if not os.path.exists(path):
            stale.append(f"{rel} (missing)")
            continue
        with open(path, encoding="utf-8", newline="") as f:
            on_disk = f.read().replace("\r\n", "\n")
        if on_disk != text:
            stale.append(rel)
    return stale


def committed_host():
    """Host and HostVersion stamped into the committed partition, so --check needs no flags."""
    with open(TABLE, encoding="utf-8") as f:
        text = f.read()
    host = re.search(r'^\s*Host = "([^"]*)",', text, flags=re.M)
    version = re.search(r'^\s*HostVersion = "([^"]*)",', text, flags=re.M)
    if not host or not version:
        raise SystemExit(f"{TABLE} has no Host/HostVersion line to rebuild from")
    return host.group(1), version.group(1)


def json_text(obj):
    return json.dumps(obj, indent=2) + "\n"


def partition_source(host, host_version):
    with open(QUERY, encoding="utf-8") as f:
        query = f.read()
    query, n_host = re.subn(r'^(\s*Host = )"[^"]*",', rf'\1"{host}",', query, flags=re.M)
    query, n_ver = re.subn(r'^(\s*HostVersion = )"[^"]*",', rf'\1"{host_version}",', query,
                           flags=re.M)
    if n_host != 1 or n_ver != 1:
        raise SystemExit("export_shared.pq no longer has exactly one Host and one HostVersion line")
    return tmdl_source(query)


def tmdl_source(query):
    """TMDL ends a multi-line expression at the first line indented less than it, so every
    line gets the same 4-tab prefix and blank lines are dropped."""
    lines = [line for line in query.splitlines() if line.strip()]
    return "\n".join("\t\t\t\t" + line for line in lines)


def project_files(name, source, columns, ids):
    """Files of a one-table PBIP whose only partition is `source` (already TMDL-indented).

    `columns` is [(column, tmdl dataType), ...]. `ids` fixes every GUID and the generator
    line, so a rebuild is byte-identical. lab/runner builds its own model with this.
    """
    files = {}

    def write(rel, text):
        files[rel] = text

    write(f"{name}.pbip", json_text({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/pbip/pbipProperties/1.0.0/schema.json",
        "version": "1.0",
        "artifacts": [{"report": {"path": f"{name}.Report"}}],
        "settings": {"enableAutoRecovery": False},
    }))
    sm = f"{name}.SemanticModel"
    write(f"{sm}/definition.pbism", json_text({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json",
        "version": "4.2", "settings": {},
    }))
    write(f"{sm}/.platform", json_text({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
        "metadata": {"type": "SemanticModel", "displayName": name},
        "config": {"version": "2.0", "logicalId": ids["model"]},
    }))
    write(f"{sm}/definition/database.tmdl", "database\n\tcompatibilityLevel: 1606\n")
    write(f"{sm}/definition/model.tmdl",
          "model Model\n"
          "\tculture: en-US\n"
          "\tdefaultPowerBIDataSourceVersion: powerBI_V3\n"
          "\tsourceQueryCulture: en-US\n"
          "\tdataAccessOptions\n"
          "\t\tlegacyRedirects\n"
          "\t\treturnErrorValuesAsNull\n"
          "\n"
          f'annotation PBI_QueryOrder = ["{name}"]\n'
          "\n"
          f"ref table {name}\n")
    column_blocks = "".join(
        f"\tcolumn {column}\n"
        f"\t\tdataType: {data_type}\n"
        f"\t\tlineageTag: {tag}\n"
        "\t\tsummarizeBy: none\n"
        f"\t\tsourceColumn: {column}\n"
        "\n"
        for (column, data_type), tag in zip(columns, ids["columns"]))
    write(f"{sm}/definition/tables/{name}.tmdl",
          f"/// Generated by {ids['generator']}. Do not edit.\n"
          f"table {name}\n"
          f"\tlineageTag: {ids['table']}\n"
          "\n"
          f"{column_blocks}"
          f"\tpartition {name} = m\n"
          "\t\tmode: import\n"
          "\t\tsource =\n"
          f"{source}\n"
          "\n"
          "\tannotation PBI_ResultType = Table\n")
    rp = f"{name}.Report"
    write(f"{rp}/definition.pbir", json_text({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/2.0.0/schema.json",
        "version": "4.0",
        "datasetReference": {"byPath": {"path": f"../{sm}"}},
    }))
    write(f"{rp}/.platform", json_text({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",
        "metadata": {"type": "Report", "displayName": name},
        "config": {"version": "2.0", "logicalId": ids["report"]},
    }))
    write(f"{rp}/definition/version.json", json_text({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/versionMetadata/1.0.0/schema.json",
        "version": "2.0.0",
    }))
    write(f"{rp}/definition/report.json", json_text({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/3.3.0/schema.json",
        "themeCollection": {"baseTheme": {
            "name": "CY25SU11",
            "reportVersionAtImport": {"visual": "2.10.0", "report": "3.4.0", "page": "2.3.1"},
            "type": "SharedResources"}},
        "resourcePackages": [{"name": "SharedResources", "type": "SharedResources", "items": [
            {"name": "CY25SU11", "path": "BaseThemes/CY25SU11.json", "type": "BaseTheme"}]}],
    }))
    write(f"{rp}/definition/pages/pages.json", json_text({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.0.0/schema.json",
        "pageOrder": ["export"], "activePageName": "export",
    }))
    write(f"{rp}/definition/pages/export/page.json", json_text({
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
        "name": "export", "displayName": "Export", "displayOption": "FitToPage",
        "height": 720, "width": 1280,
    }))
    return files


SHARED_EXPORT_IDS = {
    "generator": "lab/shared-export/build_pbip.py from export_shared.pq",
    "model": "5a4ed000-0000-4000-8000-000000000001",
    "report": "5a4ed000-0000-4000-8000-000000000002",
    "table": "5a4ed000-0000-4000-8000-000000000101",
    "columns": ["5a4ed000-0000-4000-8000-000000000102", "5a4ed000-0000-4000-8000-000000000103"],
}


def build(host, host_version):
    FILES.update(project_files(NAME, partition_source(host, host_version),
                               [("part", "int64"), ("json", "string")], SHARED_EXPORT_IDS))


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--host", default="desktop")
    parser.add_argument("--host-version", default="")
    parser.add_argument("--check", action="store_true",
                        help="rebuild in memory from the committed Host/HostVersion and fail "
                             "if the files on disk differ; writes nothing")
    args = parser.parse_args()
    if args.check:
        host, host_version = committed_host()
        build(host, host_version)
        stale = stale_files()
        if stale:
            print("SharedExport.pbip is stale against export_shared.pq. Rebuild with:\n"
                  f"  python lab/shared-export/build_pbip.py --host {host} "
                  f"--host-version {host_version}\n"
                  "Differs:\n  " + "\n  ".join(stale), file=sys.stderr)
            sys.exit(1)
        print(f"SharedExport.pbip matches export_shared.pq ({len(FILES)} files, "
              f"host={host}, version={host_version or 'unset'})")
        return
    build(args.host, args.host_version)
    flush()
    print(f"Built {os.path.join(HERE, NAME + '.pbip')} (host={args.host}, "
          f"version={args.host_version or 'unset'})")


if __name__ == "__main__":
    main()
