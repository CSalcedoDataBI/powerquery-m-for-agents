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
                                      "category": "Text.Transformations", "kind": "library"}],
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


if __name__ == "__main__":
    unittest.main()
