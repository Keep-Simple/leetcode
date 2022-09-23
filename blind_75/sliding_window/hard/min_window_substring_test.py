from collections import defaultdict

import pytest


def min_window(s, t):
    """
    Given two strings s and t of lengths m and n respectively,
    return the minimum window substring of s such
    that every character in t (including duplicates) is included in the window.
    If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.
    A substring is a contiguous sequence of characters within the string.
    """
    n = len(s)
    m = len(t)
    if n < m:
        return ""

    t_char_freq = defaultdict(int)
    window_char_freq = defaultdict(int)
    left_to_find = m
    for c in t:
        t_char_freq[c] += 1

    window_start = 0
    min_substring = ""
    min_len = n + 1

    for window_end in range(n):
        r_char = s[window_end]
        if r_char in t_char_freq:
            window_char_freq[r_char] += 1
            if window_char_freq[r_char] <= t_char_freq[r_char]:
                left_to_find -= 1

        # shrink as much as possibhle
        while left_to_find == 0:
            l_char = s[window_start]
            if l_char in t_char_freq:
                if window_char_freq[l_char] == t_char_freq[l_char]:
                    if (window_end - window_start + 1) < min_len:
                        min_substring = s[window_start : window_end + 1]
                        min_len = len(min_substring)
                    left_to_find += 1
                window_char_freq[l_char] -= 1
            window_start += 1

    return min_substring


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("bba", "ab", "ba"),
        ("aa", "aa", "aa"),
    ],
)
def test_min_window(s, t, expected):
    assert min_window(s, t) == expected
