"""
Given an array of integers where every integer occurs three times except for one integer,
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""
from collections import defaultdict


def prob40(lst):
    result = defaultdict(int)
    for val in lst:
        result[val] += 1
        if result[val] == 3:
            del(result[val])

    result = dict(result)
    return list(result.keys())[0]


if __name__ == '__main__':
    assert prob40([6, 1, 3, 3, 3, 6, 6]) == 1
    assert prob40([13, 19, 13, 13]) == 19

