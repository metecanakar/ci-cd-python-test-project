import unittest
from module_summation import do_summation


class TestSummation(unittest.TestCase):
    def test_summation(self):
        # ------------- PREPARE -----
        a = 8
        b = 6
        expected_result = 14

        # ---------- EXECUTE ---------
        result = do_summation(a, b)

        # ---------- TEST ---------
        self.assertEqual(expected_result, result)
