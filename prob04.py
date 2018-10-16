"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""


def prob04(lst):
    new_list = sorted(lst)
    try:
        idx = new_list.index(1)
        new_list = new_list[idx:]
        for idx, val in enumerate(new_list, 1):
            if idx != val:
                return idx
        return len(new_list) + 1
    except ValueError:
        return 1


if __name__ == '__main__':
    lst = [3, 4, -1, 1]
    assert prob04(lst) == 2
    lst = [1, 2, 0]
    assert prob04(lst) == 3
