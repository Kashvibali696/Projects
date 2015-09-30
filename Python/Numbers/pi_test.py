import unittest

from pi import pi_to_nth_digit


class PiToNthDigitTest(unittest.TestCase):
    def test_pi_to_nth_digit(self):
        self.assertEqual(pi_to_nth_digit(2), '3.14')
        self.assertEqual(pi_to_nth_digit(0), '3')
        self.assertEqual(pi_to_nth_digit(-1), '3.1415926535897931159979635')
        self.assertEqual(pi_to_nth_digit(30), '3.1415926535897931159979635')


if __name__ == '__main__':
    unittest.main()
