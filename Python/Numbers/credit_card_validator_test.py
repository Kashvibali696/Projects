import unittest

from credit_card_validator import validate_credit_card_number


class PiToNthDigitTest(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(Exception):
            validate_credit_card_number('siemanko')

        with self.assertRaises(Exception):
            validate_credit_card_number('1234 1234 1234 asd')

        with self.assertRaises(Exception):
            validate_credit_card_number('')

        with self.assertRaises(Exception):
            validate_credit_card_number([])

        with self.assertRaises(Exception):
            validate_credit_card_number({})

    def test_invalid_numbers(self):
        self.assertEqual(validate_credit_card_number(4929901297829863), False)
        self.assertEqual(validate_credit_card_number(5123443334705511), False)
        self.assertEqual(validate_credit_card_number(5123443334705513), False)
        self.assertEqual(validate_credit_card_number(4929901297829869), False)

    def test_valid_numbers(self):
        self.assertEqual(validate_credit_card_number(4556737586899855), True)

if __name__ == '__main__':
    unittest.main()
