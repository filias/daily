"""
Implement division of two positive integers without using the division, multiplication, or modulus operators.
Return the quotient as an integer, ignoring the remainder.
"""


def division(number1: int, number2: int) -> int:
    total, result = 0, 0
    while total < number1:
        if total + number2 > number1:
            break
        result += 1
        total += number2

    return result


assert division(4, 2) == 2
assert division(10, 5) == 2
assert division(9, 3) == 3
assert division(1, 1) == 1
assert division(9, 4) == 2
