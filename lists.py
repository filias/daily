from typing import List
"""
Given a list of numbers and a number k, return whether any two numbers from the list
add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""


def add_to_k(lst: List, k: int) -> bool:
    i = 0
    j = 1
    lst = sorted(lst)

    while i < len(lst) - 1:
        if lst[i] + lst[j] == k:
            return True
        elif lst[i] + lst[j] < k:
            j += 1
        else:
            i += 1
            j = i + 1

    return False


numbers = [10, 15, 3, 7, 5, 12, 2, 16]
k = 6
assert not add_to_k(numbers, k)

numbers = [10, 15, 3, 7]
k = 17
assert add_to_k(numbers, k)


"""
Given an array of integers, return a new array such that each element at index i of the 
new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was
[3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
from functools import reduce


def product_list(lst: List) -> List:
    output = []

    for idx, val in enumerate(lst):
        new_list = lst[:]
        new_list.remove(val)
        output.append(reduce(lambda x, y: x * y, new_list))

    return output


# Tests
lst = [3, 2, 1]
product_list(lst)

lst = [1, 2, 3, 4, 5]
assert product_list(lst) == [120, 60, 40, 30, 24]
lst = [3, 2, 1]
assert product_list(lst) == [2, 3, 6]


"""
Given an array of integers, find the first missing positive integer in linear time and 
constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""


def missing_int(lst: List) -> int:
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


lst = [3, 4, -1, 1]
assert missing_int(lst) == 2
lst = [1, 2, 0]
assert missing_int(lst) == 3


"""
Given an array of integers where every integer occurs three times except for one 
integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""
from collections import defaultdict


def non_duplicated_int(lst: List) -> int:
    result = defaultdict(int)
    for val in lst:
        result[val] += 1
        if result[val] == 3:
            del result[val]

    result = dict(result)
    return list(result.keys())[0]


assert non_duplicated_int([6, 1, 3, 3, 3, 6, 6]) == 1
assert non_duplicated_int([13, 19, 13, 13]) == 19


"""
Index i is the balance index when the condition is fulfilled
sumleft(arr, i) = sumright(arr, i)
"""


def _sum_left(lst, index):
    return sum(lst[:index])


def _sum_right(lst, index):
    # Includes the index
    return sum(lst[index:])


def balance_index(lst):
    for index, element in enumerate(lst):
        if _sum_left(lst, index) == _sum_right(lst, index):
            return index


assert balance_index([1, 2, 3, 6]) == 3
assert balance_index([5, 2, 3, 1, 1, 1, 1]) == 2


"""
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:
A researcher has index h if at least h of her N papers have h citations each. If there are multiple h satisfying this 
formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. Then the h-index would be 3, 
since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
"""


def h_index(lst: List) -> int:
    h, count = 0, 0
    lst = sorted(lst)
    for item in reversed(lst):
        if count == h and count != 0:
            return h
        else:
            h = item
            count += 1
    return h


citations = [4, 3, 0, 1, 5]
assert h_index(citations) == 3

citations = [4, 3, 0, 1, 4, 6, 5]
assert h_index(citations) == 4

citations = [1, 0]
assert h_index(citations) == 1

citations = []
assert h_index(citations) == 0
