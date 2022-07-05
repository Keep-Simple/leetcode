from typing import DefaultDict

import pytest


def find_permutation(str, pattern):
    """
    Given a string and a pattern,
    find out if the string contains any permutation of the pattern.

    Permutation is defined as the re-arranging of the characters of the string
    """
    window_start, matched = 0, 0
    diff_map = DefaultDict(int)
    for p in pattern:
        diff_map[p] += 1

    for window_end in range(len(str)):
        char = str[window_end]
        if char in diff_map:
            diff_map[char] -= 1
            if diff_map[char] == 0:
                matched += 1
        if window_end >= len(pattern):
            left_char = str[window_start]
            window_start += 1
            if left_char in diff_map:
                if diff_map[left_char] == 0:
                    matched -= 1
                diff_map[left_char] += 1
        if matched == len(diff_map):
            return True

    return False


@pytest.mark.parametrize(
    "str,pattern,expected",
    [
        ("oidbcaf", "abc", True),
        ("odicf", "dc", False),
        ("bcdxabcdy", "bcdyabcdx", True),
        ("aaacb", "abc", True),
    ],
)
def test(str, pattern, expected):
    assert find_permutation(str, pattern) == expected
