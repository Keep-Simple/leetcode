import pytest


def is_palindrome(s):
    """
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
    and removing all non-alphanumeric characters, it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
    """
    left, right = 0, len(s) - 1

    while left < right:
        if not (ch1 := _get_char(s, left)):
            left += 1
            continue
        if not (ch2 := _get_char(s, right)):
            right -= 1
            continue
        if ch1 != ch2:
            return False
        right -= 1
        left += 1

    return True


def _get_char(s, idx):
    if not s[idx].isalnum():
        return None
    return s[idx].lower()


@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ],
)
def test_is_palindrome(s, expected):
    assert is_palindrome(s) == expected
