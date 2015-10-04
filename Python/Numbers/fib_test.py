import unittest

from fib import fib


class FibSequenceTest(unittest.TestCase):
    def test_fib_seq(self):
        self.assertEqual(fib(2), [1, 1])
        self.assertEqual(fib(1), [1])
        self.assertEqual(fib(0), [])
        self.assertEqual(fib(-5), [])
        self.assertEqual(fib(3), [1, 1, 2])
        self.assertEqual(fib(5), [1, 1, 2, 3, 5])
