import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import checklist


class TestOnboarding(unittest.TestCase):
    def test_common_plus_role_items(self):
        t = {"common": ["Create account"], "IT Support": ["Issue laptop"]}
        self.assertEqual(checklist(t, "IT Support"), ["Create account", "Issue laptop"])

    def test_unknown_role_gets_common_only(self):
        t = {"common": ["Create account"]}
        self.assertEqual(checklist(t, "Other"), ["Create account"])
