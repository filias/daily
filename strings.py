def is_palindrome(x):
    return str(x) == "".join(reversed(str(x)))


assert is_palindrome("123321")
assert is_palindrome("1")
assert not is_palindrome("aabbcc")
