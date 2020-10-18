import unittest
import SpecialNumbers as sn


class TestSpecialNumber(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual("321", sn.reverse("123"))

    def test_polyndrome(self):
        self.assertEqual(True, sn.is_polyndrome(121))
