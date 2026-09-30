import json
import os
import shutil
import tempfile
import unittest

import check_examples as c
import m_blocks as mb

PAGE = """# Text.Upper

Upper case.

```m
Text.Upper("a")
```

```text
"A"
```
"""


class Blocks(unittest.TestCase):
    def test_block_with_result_after_blank_lines(self):
        [b] = mb.find_blocks("```m\n1 + 1\n```\n\n\n```text\n2\n```\n")
        self.assertEqual((b.code, b.result), ("1 + 1", "2"))

    def test_block_without_result(self):
        [b] = mb.find_blocks("```m\n1\n```\nprose\n```text\nnot its result\n```\n")
        self.assertIsNone(b.result)

    def test_unclosed_fence_is_an_error(self):
        with self.assertRaises(ValueError):
            mb.find_blocks("```m\n1\n")

    def test_apply_inserts_replaces_and_stamps_once(self):
        text = "# t\n\n```m\n1\n```\n\n```m\n2\n```\n\n```text\nold\n```\n"
        out = mb.apply_results(text, ["1", "two#(lf)lines"], "desktop", "9.9")
        self.assertEqual([b.result for b in mb.find_blocks(out)], ["1", "two#(lf)lines"])
        self.assertEqual(mb.stamp(out), ("desktop", "9.9"))
        again = mb.apply_results(out, ["1", "x"], "desktop", "10.0")
        self.assertEqual(again.count("<!-- lab:"), 1)
        self.assertEqual(mb.stamp(again), ("desktop", "10.0"))

    def test_apply_refuses_a_count_mismatch(self):
        with self.assertRaises(ValueError):
            mb.apply_results("```m\n1\n```\n", [], "desktop", "1")


class Check(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        self.ref = os.path.join(self.root, "skills", "m-reference")
        os.makedirs(os.path.join(self.ref, "generated"))
        with open(os.path.join(self.ref, "generated", "catalog.json"), "w", encoding="utf-8") as f:
            json.dump({"functions": [{"name": "Text.Upper", "file": "text-upper",
                                      "category": "Text.Transformations", "kind": "library"},
                                     {"name": "File.Contents", "file": "file-contents",
                                      "category": "Accessing data", "kind": "library"}],
                       "constants": [{"name": "JoinKind.Inner"}]}, f)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def page(self, rel, text):
        path = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return rel

    def run_check(self, *pages):
        return c.check(root=self.root, ref=self.ref, page_list=list(pages))

    def test_a_good_example_passes(self):
        p = self.page("skills/m-reference/examples/text-transformations/text-upper.md",
                      "<!-- lab: desktop 1 -->\n\n" + PAGE)
        self.assertEqual(self.run_check(p), [])

    def test_missing_result_and_stamp(self):
        p = self.page("skills/m-reference/concepts/x.md", "```m\n1\n```\n")
        errors = "\n".join(self.run_check(p))
        self.assertIn("has no ```text result", errors)
        self.assertIn("no '<!-- lab:", errors)

    def test_example_in_the_wrong_category(self):
        p = self.page("skills/m-reference/examples/text/text-upper.md",
                      "<!-- lab: desktop 1 -->\n\n" + PAGE)
        self.assertIn("examples/text-transformations/", "\n".join(self.run_check(p)))

    def test_example_without_a_card(self):
        p = self.page("skills/m-reference/examples/text-transformations/text-nope.md",
                      "<!-- lab: desktop 1 -->\n\n" + PAGE)
        self.assertIn("no card", "\n".join(self.run_check(p)))

    def test_invented_name_fails_but_engine_printed_name_passes(self):
        p = self.page("skills/m-reference/concepts/y.md",
                      "<!-- lab: desktop 1 -->\n\n`Text.Uppercase` and `Expression.Error`, "
                      "`JoinKind.Inner`.\n\n```m\nerror \"x\"\n```\n\n```text\n"
                      "error: Expression.Error: x\n```\n")
        errors = self.run_check(p)
        self.assertEqual(len(errors), 1)
        self.assertIn("'Text.Uppercase'", errors[0])

    def test_a_typo_echoed_in_an_error_message_is_not_vouched_for(self):
        p = self.page("skills/m-reference/concepts/z.md",
                      "<!-- lab: desktop 1 -->\n\n```m\nText.Uppercase(\"a\")\n```\n\n```text\n"
                      "error: Expression.Error: The name 'Text.Uppercase' wasn't recognized.\n```\n")
        self.assertIn("'Text.Uppercase'", "\n".join(self.run_check(p)))

    def test_a_typo_echoed_by_a_try_record_is_not_vouched_for(self):
        p = self.page("skills/m-reference/concepts/v.md",
                      "<!-- lab: desktop 1 -->\n\n```m\ntry Text.Uppercase(\"a\")\n```\n\n```text\n"
                      "[HasError = true, Error = [Reason = \"Expression.Error\", Message = "
                      "\"The name 'Text.Uppercase' wasn't recognized.\"]]\n```\n")
        self.assertIn("'Text.Uppercase'", "\n".join(self.run_check(p)))

    def test_any_dotted_name_in_code_is_checked_but_text_literals_are_not(self):
        p = self.page("skills/m-reference/concepts/u.md",
                      "<!-- lab: desktop 1 -->\n\n```m\n{appFigurs.Tables(), \"report.csv\"}\n```\n"
                      "\n```text\nerror: Expression.Error: x\n```\n")
        errors = self.run_check(p)
        self.assertEqual(len(errors), 1)
        self.assertIn("'appFigurs.Tables'", errors[0])

    def test_data_in_a_result_vouches_for_nothing_but_field_names_do(self):
        p = self.page("skills/m-reference/concepts/t.md",
                      "<!-- lab: desktop 1 -->\n\n`T.Name` and `Documentation.Name`.\n\n"
                      "```m\n1\n```\n\n```text\n[#\"Documentation.Name\" = \"T.Name\"]\n```\n")
        errors = self.run_check(p)
        self.assertEqual(len(errors), 1)
        self.assertIn("'T.Name'", errors[0])

    def test_names_off_the_strict_shape_are_checked_under_known_prefixes(self):
        # `Text.upper` has a lowercase second segment, so only the loose pattern sees it;
        # `catalog.md` has a prefix the export never uses and is left alone.
        p = self.page("skills/m-reference/concepts/w.md",
                      "See `Text.upper` in catalog.md.\n")
        errors = self.run_check(p)
        self.assertEqual(len(errors), 1)
        self.assertIn("'Text.upper'", errors[0])

    def block_page(self, rel, code, result):
        return self.page(rel, f"<!-- lab: desktop 1 -->\n\n```m\n{code}\n```\n\n```text\n{result}\n```\n")

    def test_a_quoted_identifier_is_the_name_it_quotes(self):
        p = self.block_page("skills/m-reference/concepts/q.md", '#"Text.Uper"("a")', '"A"')
        errors = self.run_check(p)
        self.assertEqual(len(errors), 1)
        self.assertIn("'Text.Uper'", errors[0])

    def test_a_block_that_reaches_outside_the_engine_fails(self):
        for code in ['File.Contents("x.csv")', '#"File.Contents"("x.csv")',
                     'Record.Field(#shared, "Text.Upper")']:
            with self.subTest(code=code):
                p = self.block_page("skills/m-reference/concepts/io.md", code, "1")
                errors = self.run_check(p)
                self.assertTrue(any("reach outside the engine" in e for e in errors), errors)

    def test_an_escaped_quoted_identifier_is_decoded(self):
        # #(002E) is "." in a quoted identifier, so this is File.Contents.
        p = self.block_page("skills/m-reference/concepts/esc.md",
                            '#"File#(002E)Contents"("x.csv")', "1")
        errors = self.run_check(p)
        self.assertTrue(any("File.Contents" in e and "outside the engine" in e for e in errors),
                        errors)

    def test_values_that_describe_the_machine_fail(self):
        for code in ["DateTimeZone.LocalNow()", "Culture.Current"]:
            with self.subTest(code=code):
                errors = mb.unsafe_calls(code, {"functions": []})
                self.assertEqual(errors, [code.split("(")[0]])

    def test_the_runner_refuses_names_the_export_does_not_have(self):
        # The live #shared can hold a connector the committed export does not.
        catalog = {"functions": [], "constants": [{"name": "JoinKind.Inner"}]}
        self.assertEqual(mb.unsafe_calls('New.Connector("x")', catalog, unknown=True),
                         ["New.Connector"])
        self.assertEqual(mb.unsafe_calls('New.Connector("x")', catalog), [])
        self.assertEqual(mb.unsafe_calls('{JoinKind.Inner, #"Step one"}', catalog, unknown=True), [])

    def test_names_in_text_literals_and_comments_call_nothing(self):
        p = self.block_page("skills/m-reference/concepts/lit.md",
                            '"File.Contents" // File.Contents', '"File.Contents"')
        self.assertEqual(self.run_check(p), [])


if __name__ == "__main__":
    unittest.main()
