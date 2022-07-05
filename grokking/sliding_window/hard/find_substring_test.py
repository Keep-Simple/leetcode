from typing import DefaultDict

import pytest


def find_substring(str, pattern):
    """
    Given a string and a pattern,
    find the smallest substring in the given string
    which has all the character occurrences of the given pattern.
    """
    window_start = matches = 0
    min_substring = []
    freq_map = DefaultDict(int)
    for p in pattern:
        freq_map[p] += 1

    for window_end in range(len(str)):
        char = str[window_end]

        if char in freq_map:
            freq_map[char] -= 1
            if freq_map[char] == 0:
                matches += 1

        while matches == len(freq_map):
            min_substring = (
                str[window_start : window_end + 1]
                if not min_substring or len(min_substring) > window_end - window_end + 1
                else min_substring
            )
            left_char = str[window_start]
            window_start += 1
            if left_char in freq_map:
                if freq_map[left_char] == 0:
                    matches -= 1
                freq_map[left_char] += 1

    return "".join(min_substring)


@pytest.mark.parametrize(
    "str,pattern,expected",
    [
        ("aabdec", "abc", "abdec"),
        ("aabdec", "abac", "aabdec"),
        ("abdbca", "abc", "bca"),
        ("adcad", "abc", ""),
    ],
)
def test(str, pattern, expected):
    assert find_substring(str, pattern) == expected
