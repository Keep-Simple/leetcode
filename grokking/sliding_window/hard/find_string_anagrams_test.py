from typing import DefaultDict

import pytest


def find_string_anagrams(str, pattern):
    """
    Given a string and a pattern,
    find all anagrams of the pattern in the given string.

    Every anagram is a permutation of a string
    """
    window_start, matched = 0, 0
    diff_map = DefaultDict(int)
    anagrams_indexes = []
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
            anagrams_indexes.append(window_start)

    return anagrams_indexes


@pytest.mark.parametrize(
    "str,pattern,expected",
    [
        ("ppqp", "pq", [1, 2]),
        ("abbcabc", "abc", [2, 3, 4]),
    ],
)
def test(str, pattern, expected):
    assert find_string_anagrams(str, pattern) == expected
