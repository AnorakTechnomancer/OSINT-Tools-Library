import unittest
from pathlib import Path
from validate_tool_metadata import validate_text
from generate_category_tables import cell, table, load_tools

class MetadataTests(unittest.TestCase):
    def setUp(self):
        self.text = (Path(__file__).resolve().parents[1] / 'osint-tools/wayback-machine.md').read_text()

    def test_pending_verification_requires_explanation(self):
        self.assertFalse(validate_text(self.text)[1])
        lines = self.text.splitlines()
        start = next(i for i, line in enumerate(lines) if line.startswith('  verification_notes:'))
        end = start + 1
        while end < len(lines) and lines[end].startswith('    '): end += 1
        del lines[start:end]
        self.assertIn('unverified tools require verification_notes', validate_text('\n'.join(lines))[1])

    def test_bad_date_and_access_are_rejected(self):
        bad = self.text.replace('last_verified: null', 'last_verified: 2026-02-30').replace('- online-web', '- made-up-access')
        self.assertEqual(len(validate_text(bad)[1]), 2)

    def test_yaml_yes_no_are_not_booleans(self):
        self.assertFalse(validate_text(self.text.replace("account_required: 'no'", 'account_required: no'))[1])

    def test_generated_table_contains_all_archive_tools(self):
        generated = table('archiving', load_tools())
        self.assertEqual(len(generated.splitlines()), 14)
        self.assertIn('Browser extension · Online/Web · CLI', generated)
        self.assertIn('Pending', generated)

    def test_table_escapes_delimiters(self):
        self.assertEqual(cell('a|b\nc'), 'a&#124;b c')

if __name__ == '__main__': unittest.main()
