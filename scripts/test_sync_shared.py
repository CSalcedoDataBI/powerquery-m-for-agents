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

    def catalog_dir(self):
        return os.path.join(self.ref, "catalog")

    def run_sync(self, *paths, **kw):
        kw.setdefault("min_functions", 1)
        return s.sync(list(paths), ref=self.ref, write=True, catalog_dir=self.catalog_dir(), **kw)

    def catalog(self):
        catalog = s.load_catalog(self.catalog_dir())
        return {r["name"]: r for r in catalog["functions"]}

    def card(self, name):
        """The `## <name>` section of the packed file the catalogue says holds it."""
        text = self.generated(f"library/{self.catalog()[name]['card']}.md")
        return dict(s.sections(text))[name]

    def generated(self, name):
        with open(os.path.join(self.ref, "generated", name), encoding="utf-8") as f:
            return f.read()

    def test_cards_are_packed_one_file_per_part(self):
        self.run_sync(DESKTOP)
        files = sorted(os.listdir(os.path.join(self.ref, "generated", "library")))
        cat = self.catalog()
        self.assertEqual(files, sorted({f"{r['card']}.md" for r in cat.values()}))
        self.assertLess(len(files), len(cat))
        for name, row in cat.items():
            self.assertEqual(row["card"], s.catalog_part(row), name)
            self.assertIn(f"{name}(", self.card(name))
        # The catalogue row names the file, so the agent opens one file and one section.
        self.assertIn("| table |", self.generated("catalog.md"))
        self.assertIn("| connectors |", self.generated("connectors.md"))

    def test_a_part_over_the_limit_continues_in_a_second_file(self):
        rows = [{"name": f"Table.F{i}", "kind": "library", "category": "Table"} for i in range(3)]
        sections = {r["name"]: f"## {r['name']}\n\n" + "x" * 600 + "\n" for r in rows}
        files = s.pack_cards(rows, sections, [], limit=1024 + 1300)
        self.assertEqual(sorted(files), ["table", "table-2"])
        self.assertEqual([r["card"] for r in rows], ["table", "table", "table-2"])
        self.assertEqual([n for n, _ in s.sections(files["table-2"])], ["Table.F2"])

    def test_sections_ignore_headings_inside_code(self):
        text = "# t\n\n## A.B\n\n```m\n## not a heading\n```\n\n## C.D\n\nx\n"
        self.assertEqual([n for n, _ in s.sections(text)], ["A.B", "C.D"])

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
        # Constant descriptions come from Microsoft's MIT file, never from the engine.
        self.run_sync(DESKTOP, descriptions={
            "JoinKind.Inner": "A possible kind of join. The inner join contains a row for each match.",
            "Int64.Type": "A 64-bit integer | pipe."})
        md = self.generated("constants.md")
        self.assertIn("| `JoinKind.Inner` | number | `0` |", md)
        # The row keeps the sentence after the shared first one.
        self.assertIn("inner join contains a row", md)
        self.assertIn("| `Int64.Type` | type |  |", md)
        self.assertIn("64-bit integer \\| pipe", md)
        self.assertNotIn("Broken.Constant", md)
        self.assertIn("2 constants and type values in `constants.md`", self.generated("catalog.md"))

    def test_the_catalogue_is_split_and_reads_back_whole(self):
        self.run_sync(DESKTOP)
        folder = self.catalog_dir()
        self.assertFalse(os.path.exists(os.path.join(self.ref, "generated", "catalog")))
        with open(os.path.join(folder, "index.json"), encoding="utf-8") as f:
            parts = json.load(f)["parts"]
        self.assertGreater(len(parts), 1)
        catalog = s.load_catalog(folder)
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

    def test_cards_quote_only_licensed_text(self):
        # Option B of #1: the description is Microsoft's MIT text or nothing; the engine's
        # own examples are not copied; a Learn link only for a page that was checked.
        self.run_sync(DESKTOP, descriptions={"Table.AddColumn": "Adds a column named newColumnName."},
                      learn=("https://learn.example/", {"table-addcolumn"}))
        card = self.card("Table.AddColumn")
        self.assertIn("Adds a column named newColumnName.", card)
        self.assertIn("*Description: Microsoft, MIT", card)
        self.assertIn("Reference: [Microsoft Learn](https://learn.example/table-addcolumn)", card)
        self.assertNotIn("Examples (engine metadata", card)
        undescribed = self.card("List.Sum")
        self.assertNotIn("Description: Microsoft", undescribed)
        self.assertNotIn("Microsoft Learn", undescribed)
        self.assertNotIn("Examples (engine metadata", undescribed)

    def test_export_without_constants_does_not_flag_them_partial(self):
        # excel-fixture predates the constants export: it contributes no hosts to them.
        self.run_sync(DESKTOP, EXCEL, accept_count_change=True)
        constants = {c["name"]: c for c in
                     s.load_catalog(self.catalog_dir())["constants"]}
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
        card = self.card("List.Sum")
        self.assertIn("optional precision as nullable number", card)

    def test_notes_and_examples_set_flags(self):
        os.makedirs(os.path.join(self.ref, "notes"))
        write(os.path.join(self.ref, "notes", "list-sum.md"), "# note\n")
        ex = os.path.join(self.ref, "examples")
        os.makedirs(ex)
        write(os.path.join(ex, "list-addition.md"),
              "# x\n\n## List.Sum\n\n```m\n1\n```\n```m\n2\n```\n\n## List.Other\n\n```m\n3\n```\n")
        self.run_sync(DESKTOP)
        row = self.catalog()["List.Sum"]
        self.assertTrue(row["notes"])
        self.assertEqual(row["examples"], 2)
        self.assertIn("examples/list-addition.md", self.card("List.Sum"))
        self.assertIn("section `## List.Sum`", self.card("List.Sum"))

    def test_orphan_note_refuses(self):
        os.makedirs(os.path.join(self.ref, "notes"))
        write(os.path.join(self.ref, "notes", "table-nope.md"), "x")
        with self.assertRaises(s.GateError):
            self.run_sync(DESKTOP)
        self.assertFalse(os.path.exists(os.path.join(self.ref, "generated")))
        self.assertFalse(os.path.exists(self.catalog_dir()))

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
        s.sync([DESKTOP], ref=self.ref, write=False, min_functions=1,
               catalog_dir=self.catalog_dir())
        self.assertFalse(os.path.exists(os.path.join(self.ref, "generated")))
        self.assertFalse(os.path.exists(self.catalog_dir()))

    def test_chunked_export_is_reassembled(self):
        payload = open(DESKTOP, encoding="utf-8").read()
        chunks = [{"part": i, "json": payload[i * 50:(i + 1) * 50]}
                  for i in range((len(payload) + 49) // 50)]
        path = os.path.join(self.ref, "chunked.json")
        write(path, json.dumps(list(reversed(chunks))))
        self.assertEqual(len(s.load_export(path)["functions"]), 7)


if __name__ == "__main__":
    unittest.main()
