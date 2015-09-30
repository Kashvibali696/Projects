import unittest

from e import e_to_nth_digit


class PiToNthDigitTest(unittest.TestCase):
    def test_pi_to_nth_digit(self):
        self.assertEqual(e_to_nth_digit(2), '2.72')
        self.assertEqual(e_to_nth_digit(0), '3')
        self.assertEqual(e_to_nth_digit(-1), '2.7182818284590450907955983')
        self.assertEqual(e_to_nth_digit(30), '2.7182818284590450907955983')


if __name__ == '__main__':
    unittest.main()
