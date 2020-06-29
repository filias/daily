"""
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and
character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have
no digits and consists solely of alphabetic characters. You can assume the string to be
decoded is valid.
"""


def encode(str):
    char_count = 0
    current_char = ""
    result = ""
    for char in str:
        if current_char == "":
            current_char = char
            char_count += 1
        elif char == current_char:
            char_count += 1
        else:
            result += "{}{}".format(char_count, current_char)
            current_char = char
            char_count = 1

    # Put the last char
    result += "{}{}".format(char_count, current_char)

    return result


def decode(str):
    result = ""
    char_count = 0
    for char in str:
        if char.isdigit():
            char_count = int(char)
        else:
            result += char * char_count

    return result


assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"
assert decode("4A3B2C1D2A") == "AAAABBBCCDAA"
