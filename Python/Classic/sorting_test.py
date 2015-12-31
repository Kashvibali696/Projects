from __future__ import unicode_literals

import unittest

from sorting import bubble_sort, merge_sort


class SortingTests(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(bubble_sort([1, 3, 2, 11, 5]), [1, 2, 3, 5, 11])
        self.assertEqual(bubble_sort([5, -1, 0, 2, 3]), [-1, 0, 2, 3, 5])
        self.assertEqual(bubble_sort([3]), [3])

    def test_merge_sort(self):
        self.assertEqual([], merge_sort([]))
        self.assertEqual(bubble_sort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(bubble_sort([1, 3, 2, 11, 5]), [1, 2, 3, 5, 11])
        self.assertEqual(bubble_sort([5, -1, 0, 2, 3]), [-1, 0, 2, 3, 5])
        self.assertEqual(bubble_sort([3]), [3])


if __name__ == '__main__':
    unittest.main()
