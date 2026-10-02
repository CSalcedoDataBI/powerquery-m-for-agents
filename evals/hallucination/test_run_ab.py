"""Tests for the invented-name counter. No API calls.

  python -m unittest discover -s evals/hallucination -t evals/hallucination
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import run_ab  # noqa: E402

NAMES, ROWS = run_ab.catalog_names()


class CatalogTest(unittest.TestCase):
    def test_catalogue_is_the_export(self):
        self.assertIn("Table.AddColumn", NAMES)
        self.assertIn("Int64.Type", NAMES)          # constants count as real names
        self.assertIn("BinaryFormat.Byte", NAMES)

    def test_every_question_has_rows_for_its_category(self):
        for q in run_ab.load_questions():
            with self.subTest(q=q["id"]):
                self.assertIn(q["category"], ROWS)
                self.assertTrue(ROWS[q["category"]])

    def test_traps_do_not_exist(self):
        # A trap Microsoft ships later must fail here, not silently become a real answer.
        for q in run_ab.load_questions():
            for trap in q.get("traps", []):
                with self.subTest(q=q["id"], trap=trap):
                    self.assertNotIn(trap, NAMES)

    def test_ids_unique_and_regimes_known(self):
        qs = run_ab.load_questions()
        self.assertEqual(len({q["id"] for q in qs}), len(qs))
        self.assertEqual({q["regime"] for q in qs}, {"core", "deep"})

    def test_names_written_in_questions_exist(self):
        # A question that itself names a function must name a real one.
        for q in run_ab.load_questions():
            for name in run_ab.used_names("`" + q["question"].replace("`", "") + "`"):
                if not name.startswith("#"):
                    with self.subTest(q=q["id"], name=name):
                        self.assertIn(name, NAMES)


class CounterTest(unittest.TestCase):
    def test_invented_dotted_name_in_fence(self):
        text = "Use this:\n```m\nText.Left([Name], 3)\n```"
        self.assertEqual(run_ab.invented(text, NAMES), ["Text.Left"])

    def test_real_names_are_not_invented(self):
        text = "```powerquery\nTable.AddColumn(t, \"x\", each Text.Start([Name], 3), type text)\n```"
        self.assertEqual(run_ab.invented(text, NAMES), [])

    def test_prose_is_not_counted(self):
        self.assertEqual(run_ab.invented("Text.Left does not exist in M.", NAMES), [])

    def test_inline_code_is_counted(self):
        self.assertEqual(run_ab.invented("Call `List.RunningSum(xs)`.", NAMES),
                         ["List.RunningSum"])

    def test_strings_comments_and_step_names_are_ignored(self):
        code = ('```m\nlet\n  #"Sales.Amount" = 1, // Text.Left here\n'
                '  s = "Text.Right"\nin s\n```')
        self.assertEqual(run_ab.invented(code, NAMES), [])

    def test_field_access_is_not_a_library_name(self):
        code = "```m\neach [Sales.Amount] * 2\n```"
        self.assertEqual(run_ab.invented(code, NAMES), [])

    def test_defined_field_names_are_not_library_names(self):
        code = ('```m\nfn meta [\n  Documentation.Name = "Add",\n'
                '  Documentation.Examples = {}\n]\n```')
        self.assertEqual(run_ab.invented(code, NAMES), [])
        # A metadata field named in prose is a field, not a function.
        self.assertEqual(run_ab.invented("Set `Documentation.Name`.", NAMES), [])
        self.assertFalse([n for n in NAMES if n.startswith(run_ab.METADATA_PREFIXES)])
        # ...but a made-up name used as a value still counts.
        self.assertEqual(run_ab.invented("```m\n[x = Foo.Bar(1)]\n```", NAMES), ["Foo.Bar"])

    def test_hash_literals(self):
        ok = "```m\n#date(2024, 1, 1) + #duration(1, 0, 0, 0)\n```"
        self.assertEqual(run_ab.invented(ok, NAMES), [])
        bad = "```m\n#money(10)\n```"
        self.assertEqual(run_ab.invented(bad, NAMES), ["#money"])

    def test_each_name_counted_once(self):
        code = "```m\nText.Left(a, 1) & Text.Left(b, 1)\n```"
        self.assertEqual(run_ab.invented(code, NAMES), ["Text.Left"])

    def test_empty_answer(self):
        self.assertEqual(run_ab.invented("", NAMES), [])
        self.assertEqual(run_ab.silent([{"A": {"text": ""}, "B": {"text": "x"}}]),
                         {"A": 1, "B": 0})


class PairingTest(unittest.TestCase):
    def rec(self, a, b, ra=None, rb=None):
        return {"id": "q", "regime": "core",
                "A": {"text": a, "stop_reason": ra}, "B": {"text": b, "stop_reason": rb}}

    def test_refused_question_is_dropped_not_scored(self):
        bad = "```m\nText.Left(x, 1)\n```"
        records = [self.rec(bad, "", None, "refusal"), self.rec(bad, "ok")]
        s = run_ab.summarise(records, NAMES)["core"]
        self.assertEqual((s["n"], s["dropped"], s["A"], s["B"]), (1, 1, 1, 0))
        self.assertEqual(run_ab.refusals(records), ["q B"])

    def test_resume_reasks_empty_without_reason_keeps_refusal(self):
        import json
        import tempfile
        path = os.path.join(tempfile.mkdtemp(), "run.json")
        records = [dict(self.rec("a", ""), id="empty"),
                   dict(self.rec("a", "", None, "refusal"), id="refused"),
                   dict(self.rec("a", "b"), id="done")]
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"records": records}, f)
        self.assertEqual(sorted(run_ab.already_answered(path)), ["done", "refused"])


class ProviderTest(unittest.TestCase):
    def test_known_prefixes(self):
        self.assertEqual(run_ab.provider_for("claude-haiku-4-5-20251001")[0], "anthropic")
        self.assertEqual(run_ab.provider_for("deepseek-v4-flash")[0], "deepseek")

    def test_unknown_prefix_stops(self):
        with self.assertRaises(SystemExit):
            run_ab.provider_for("gpt-5")

    def test_arm_b_carries_rows_arm_a_does_not(self):
        a = run_ab._anthropic_request("claude-x", "Q?", None, "S", 10)
        b = run_ab._anthropic_request("claude-x", "Q?", "- Text.Start: x", "S", 10)
        self.assertEqual(a["messages"][0]["content"], "Q?")
        self.assertIn("- Text.Start: x", b["messages"][0]["content"])


if __name__ == "__main__":
    unittest.main()
