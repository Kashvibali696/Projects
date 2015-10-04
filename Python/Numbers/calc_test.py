import unittest

from calc import calculate, WrongArgumentTypeException


class CalcTests(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises():
            pass

    def test_addition(self):
        self.assertEqual("2 + 2", 4)
        self.assertEqual("2 + (-2)", 0)
        self.assertEqual("   2     +    1 ", 3)
        self.assertEqual("-2 + 2 ", 0)
        self.assertEqual("2 + 3 + 4", 9)
        self.assertEqual("1 + 1 + 1 + 1 + 1 + 1", 6)
        self.assertEqual("1.5 + 1.5", 3.0)
        self.assertEqual("1.1 + 2 + 1.3", 4.4)
        self.assertEqual("2. + 2.", 4.0)

    def test_subtraction(self):
        self.assertEqual("2 - 2", 0)
        self.assertEqual("2 - 4", -2)
        self.assertEqual("4 - 4 + 2 - 11", 9)
        self.assertEqual("1.5 - 1.4", 0.1)


if __name__ == '__main__':
    unittest.main()
