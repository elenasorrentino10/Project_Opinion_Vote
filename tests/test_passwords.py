import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'project'))

from libraries.passwords import hash_password, verify_password  # noqa: E402


class PasswordTests(unittest.TestCase):
    def test_correct_password_is_accepted(self):
        self.assertTrue(verify_password('secret', hash_password('secret')))

    def test_wrong_password_is_rejected(self):
        self.assertFalse(verify_password('wrong', hash_password('secret')))

    def test_password_is_not_stored_in_clear(self):
        self.assertNotIn('secret', hash_password('secret'))

    def test_same_password_gets_a_different_hash(self):
        self.assertNotEqual(hash_password('secret'), hash_password('secret'))

    def test_value_in_an_old_format_is_rejected(self):
        self.assertFalse(verify_password('secret', 'secret'))


if __name__ == '__main__':
    unittest.main()
