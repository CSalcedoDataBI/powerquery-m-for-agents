import json
import os
import shutil
import tempfile
import unittest

import sync_shared as s

HERE = os.path.dirname(os.path.abspath(__file__))
DESKTOP = os.path.join(HERE, "fixtures", "desktop-fixture.json")
EXCEL = os.path.join(HERE, "fixtures", "excel-fixture.json")


def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


class Names(unittest.TestCase):
    def test_card_file(self):
        self.assertEqual(s.card_file("Table.AddColumn"), "table-addcolumn")
        self.assertEqual(s.card_file("#date"), "hash-date")
        self.assertEqual(s.card_file("#table"), "hash-table")

    def test_category_falls_back_to_prefix_then_none(self):
        self.assertEqual(s.category_of({"name": "List.Sum", "category": None}), "List")
        self.assertEqual(s.category_of({"name": "#date"}), "(none)")

    def test_signature_marks_optional(self):
        with open(DESKTOP, encoding="utf-8") as f:
            fn = json.load(f)["functions"][0]
        self.assertEqual(s.signature(fn),
                         "Table.AddColumn(table as table, newColumnName as text, "
                         "columnGenerator as function, optional columnType as nullable type)"
                         " as table")


class CleanText(unittest.TestCase):
    def test_html_becomes_markdown(self):
        raw = ("Groups <code>table</code> rows.<br>\n    <ul><li>One</li><li>Two</li></ul>"
               "\n    Use &quot;x&quot;.")
        self.assertEqual(s.clean_text(raw), 'Groups `table` rows.\n\n- One\n- Two\n\nUse "x".')

    def test_no_line_keeps_code_block_indentation(self):
        out = s.clean_text("First.\n        Second, indented as in the C# source.")
        self.assertFalse(any(line.startswith("    ") for line in out.splitlines()))


class Sync(unittest.TestCase):
    def setUp(self):
        self.ref = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.ref, ignore_errors=True)

    def run_sync(self, *paths, **kw):
        kw.setdefault("min_functions", 1)
        return s.sync(list(paths), ref=self.ref, write=True, **kw)

    def catalog(self):
        catalog = s.load_catalog(os.path.join(self.ref, "generated"))
        return {r["name"]: r for r in catalog["functions"]}

    def generated(self, name):
        with open(os.path.join(self.ref, "generated", name), encoding="utf-8") as f:
            return f.read()

    def test_writes_one_card_per_usable_function(self):
        self.run_sync(DESKTOP)
        cards = sorted(os.listdir(os.path.join(self.ref, "generated", "library")))
        self.assertEqual(cards, ["csv-document.md", "hash-date.md", "list-hidden.md",
                                 "list-sum.md", "mixpanel-tables.md", "table-addcolumn.md"])

    def test_connectors_split_from_the_library(self):
        self.run_sync(DESKTOP)
        cat = self.catalog()
        self.assertEqual(cat["Mixpanel.Tables"]["kind"], "connector")
        # "Accessing data" is a library category; a dotless name and an uncategorised
        # function under a library prefix stay in the library too.
        for name in ("Csv.Document", "#date", "List.Hidden", "Table.AddColumn"):
            self.assertEqual(cat[name]["kind"], "library", name)
        catalog_md, connectors_md = self.generated("catalog.md"), self.generated("connectors.md")
        self.assertNotIn("`Mixpanel.Tables`", catalog_md)
        self.assertIn("| `Mixpanel.Tables` | Mixpanel |", connectors_md)
        self.assertNotIn("`Csv.Document`", connectors_md)
        self.assertIn("1 connector entry points are in `connectors.md`", catalog_md)

    def test_constants_index(self):
        self.run_sync(DESKTOP)
        md = self.generated("constants.md")
        self.assertIn("| `JoinKind.Inner` | number | `0` |", md)
        # The row keeps the sentence after the enum's shared first one.
        self.assertIn("inner join contains a row", md)
        self.assertIn("| `Int64.Type` | type |  |", md)
        self.assertIn("64-bit integer \\| pipe", md)
        self.assertNotIn("Broken.Constant", md)
        self.assertIn("2 constants and type values in `constants.md`", self.generated("catalog.md"))

    def test_the_catalogue_is_split_and_reads_back_whole(self):
        self.run_sync(DESKTOP)
        folder = os.path.join(self.ref, "generated", "catalog")
        self.assertFalse(os.path.exists(os.path.join(self.ref, "generated", "catalog.json")))
        with open(os.path.join(folder, "index.json"), encoding="utf-8") as f:
            parts = json.load(f)["parts"]
        self.assertGreater(len(parts), 1)
        catalog = s.load_catalog(os.path.join(self.ref, "generated"))
        names = [r["name"] for r in catalog["functions"]]
        self.assertEqual(names, sorted(names, key=str.lower))
        on_disk = 0
        for part in parts:
            with open(os.path.join(folder, part + ".json"), encoding="utf-8") as f:
                rows = json.load(f)["functions"]
            on_disk += len(rows)
            self.assertEqual({s.catalog_part(r) for r in rows}, {part})
        self.assertEqual(on_disk, len(names))
        self.assertTrue(catalog["constants"])

    def test_export_without_constants_does_not_flag_them_partial(self):
        # excel-fixture predates the constants export: it contributes no hosts to them.
        self.run_sync(DESKTOP, EXCEL, accept_count_change=True)
        constants = {c["name"]: c for c in
                     s.load_catalog(os.path.join(self.ref, "generated"))["constants"]}
        self.assertEqual(constants["JoinKind.Inner"]["hosts"], ["desktop"])
        self.assertFalse(constants["JoinKind.Inner"]["partialHosts"])
        # ...and is not named as a source of constants.md either.
        header = self.generated("constants.md").splitlines()[2]
        self.assertIn("`desktop`", header)
        self.assertNotIn("`excel`", header)

    def test_no_constants_index_when_no_export_has_them(self):
        self.run_sync(EXCEL)
        self.assertFalse(os.path.exists(os.path.join(self.ref, "generated", "constants.md")))
        self.assertNotIn("constants.md", self.generated("catalog.md"))

    def test_export_errors_are_skipped(self):
        self.run_sync(DESKTOP)
        self.assertNotIn("Broken.Function", self.catalog())

    def test_hosts_merge_and_partial_flag(self):
        self.run_sync(DESKTOP, EXCEL)
        cat = self.catalog()
        self.assertEqual(cat["List.Sum"]["hosts"], ["desktop", "excel"])
        self.assertFalse(cat["List.Sum"]["partialHosts"])
        self.assertTrue(cat["Table.AddColumn"]["partialHosts"])
        md = open(os.path.join(self.ref, "generated", "catalog.md"), encoding="utf-8").read()
        self.assertIn("⌂", md)

    def test_first_export_wins_the_card(self):
        self.run_sync(DESKTOP, EXCEL)
        card = open(os.path.join(self.ref, "generated", "library", "list-sum.md"),
                    encoding="utf-8").read()
        self.assertIn("optional precision as nullable number", card)

    def test_notes_and_examples_set_flags(self):
        os.makedirs(os.path.join(self.ref, "notes"))
        write(os.path.join(self.ref, "notes", "list-sum.md"), "# note\n")
        ex = os.path.join(self.ref, "examples", "list-addition")
        os.makedirs(ex)
        write(os.path.join(ex, "list-sum.md"), "```m\n1\n```\n```m\n2\n```\n")
        self.run_sync(DESKTOP)
        row = self.catalog()["List.Sum"]
        self.assertTrue(row["notes"])
        self.assertEqual(row["examples"], 2)

    def test_orphan_note_refuses(self):
        os.makedirs(os.path.join(self.ref, "notes"))
        write(os.path.join(self.ref, "notes", "table-nope.md"), "x")
        with self.assertRaises(s.GateError):
            self.run_sync(DESKTOP)
        self.assertFalse(os.path.exists(os.path.join(self.ref, "generated")))

    def test_small_export_refuses(self):
        with self.assertRaises(s.GateError):
            self.run_sync(DESKTOP, min_functions=100)

    def test_count_drift_refuses_unless_accepted(self):
        self.run_sync(DESKTOP)
        with self.assertRaises(s.GateError):
            self.run_sync(EXCEL)
        self.assertEqual(len(self.catalog()), 6, "previous generated/ must survive")
        self.run_sync(EXCEL, accept_count_change=True)
        self.assertEqual(len(self.catalog()), 2)

    def test_report_mode_writes_nothing(self):
        s.sync([DESKTOP], ref=self.ref, write=False, min_functions=1)
        self.assertFalse(os.path.exists(os.path.join(self.ref, "generated")))

    def test_chunked_export_is_reassembled(self):
        payload = open(DESKTOP, encoding="utf-8").read()
        chunks = [{"part": i, "json": payload[i * 50:(i + 1) * 50]}
                  for i in range((len(payload) + 49) // 50)]
        path = os.path.join(self.ref, "chunked.json")
        write(path, json.dumps(list(reversed(chunks))))
        self.assertEqual(len(s.load_export(path)["functions"]), 7)


if __name__ == "__main__":
    unittest.main()
