import unittest

from decimal import Decimal


class TestDecimalMethods(unittest.TestCase):

    def test_add_float(self):
        sum = Decimal(0.1).add(Decimal(0.2))
        expected_res = Decimal(0.3)

        self.assertEqual(sum.is_equal(expected_res), True)

if __name__ == '__main__': # pragma: no cover
    unittest.main()