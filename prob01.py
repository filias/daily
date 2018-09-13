"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def prob01(lst, k):
    i = 0
    j = 1
    lst = sorted(lst)

    while i < len(lst) - 1:
        if lst[i] + lst[j] == k:
            print('true')
            return True
        elif lst[i] + lst[j] < k:
            j += 1
        else:
            i += 1
            j = i + 1

    print('false')
    return False


if __name__ == '__main__':
    lst = [10, 15, 3, 7, 5, 12, 2, 16]
    k = 6
    prob01(lst, k)
