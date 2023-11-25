import unittest


class TestCalcMethods(unittest.TestCase):

    def test_add_float(self):
        self.assertNotEqual(0.1 + 0.2, 0.3)

if __name__ == '__main__': # pragma: no cover
    unittest.main()