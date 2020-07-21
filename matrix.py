"""You are given a 2-d matrix where each cell represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down, find the maximum
number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1

The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins."""
from typing import List, Tuple


def collect_coins(matrix):
    def collect_coins_aux(position: Tuple, path: List):

        row = position[0]
        column = position[1]

        # Add the current position value to the path
        path.append(matrix[row][column])

        # Stop condition
        if position == (rows - 1, columns - 1):
            return

        if column == columns - 1:
            # Can only go down
            collect_coins_aux((row + 1, column), path)
        elif row == rows - 1:
            # Can only go right
            collect_coins_aux((row, column + 1), path)
        else:
            # Can go down and right - create a new path
            new_path = path[:]
            paths.append(new_path)
            collect_coins_aux((row + 1, column), new_path)
            collect_coins_aux((row, column + 1), path)

    paths = [[]]
    rows = len(matrix)
    columns = len(matrix[0])

    # Empty matrix
    if matrix == paths:
        return 0

    # Position (row, column)
    collect_coins_aux((0, 0), paths[0])

    return max([sum(path) for path in paths])


matrix = [[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]]
assert collect_coins(matrix) == 12
matrix = [[]]
assert collect_coins(matrix) == 0
