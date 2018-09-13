import unittest

from prob01 import prob01
from prob02 import prob02


class TestDailyProblems(unittest.TestCase):

    def test_prob01(self):
        lst = [10, 15, 3, 7]
        k = 17
        self.assertTrue(prob01(lst, k))

    def test_prob02(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(prob02(lst), [120, 60, 40, 30, 24])

        lst = [3, 2, 1]
        self.assertEqual(prob02(lst), [2, 3, 6])


if __name__ == '__main__':
    unittest.main()
