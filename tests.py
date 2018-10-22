import unittest

from prob01 import prob01
from prob02 import prob02
from prob03 import serialize, deserialize, Node
from prob04 import prob04
from prob29 import encode, decode
from prob40 import prob40


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

    def test_prob03(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        print(serialize(node))
        self.assertEqual(deserialize(serialize(node)).left.left.val, 'left.left')

    def test_prob04(self):
        lst = [3, 4, -1, 1]
        self.assertEqual(prob04(lst), 2)
        lst = [1, 2, 0]
        self.assertEqual(prob04(lst), 3)

    def test_prob29(self):
        self.assertEqual(encode("AAAABBBCCDAA"), "4A3B2C1D2A")
        self.assertEqual(decode("4A3B2C1D2A"), "AAAABBBCCDAA")

    def test_prob40(self):
        self.assertEqual(prob40([6, 1, 3, 3, 3, 6, 6]), 1)
        self.assertEqual(prob40([13, 19, 13, 13]), 19)


if __name__ == '__main__':
    unittest.main()
