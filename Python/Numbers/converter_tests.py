from converter import bin2dec, dec2bin, WrongArgumentException

import unittest


class Dec2BinTest(unittest.TestCase):

    def test_convert(self):
        self.assertEqual(dec2bin(10), '1010')
        self.assertEqual(dec2bin(0), '0')
        self.assertEqual(dec2bin(1), '1')
        self.assertEqual(dec2bin(5), '101')

    def test_with_exception(self):
        with self.assertRaises(WrongArgumentException):
            dec2bin(-1000)

        with self.assertRaises(WrongArgumentException):
            dec2bin('asdasd')

        with self.assertRaises(WrongArgumentException):
            dec2bin(2.5)


class Bin2DecTest(unittest.TestCase):

    def test_convert_positive(self):
        self.assertEqual(bin2dec(11), 3)
        self.assertEqual(bin2dec(01), 1)
        self.assertEqual(bin2dec(1111), 15)
        self.assertEqual(bin2dec('1111'), 15)

    def test_convert_with_exception(self):
        with self.assertRaises(WrongArgumentException):
            bin2dec(-1000)

        with self.assertRaises(WrongArgumentException):
            bin2dec(43231)

        with self.assertRaises(WrongArgumentException):
            bin2dec('asdasd')

        with self.assertRaises(WrongArgumentException):
            bin2dec('12345')


if __name__ == '__main__':
    unittest.main()
