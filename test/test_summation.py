import unittest
from module_summation import do_summation

class TestSummation(unittest.TestCase):
    def test_summation(self):
        # ------------- PREPARE -----
        a = 6
        b = 7
        expected_result = 13

        # ---------- EXECUTE ---------
        result = do_summation(a, b)

        self.assertEqual(expected_result, result)