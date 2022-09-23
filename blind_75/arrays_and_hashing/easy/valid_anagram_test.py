from collections import defaultdict

import pytest


def is_anagram(s, t):
    """
    Given two strings s and t,
    return true if t is an anagram of s,
    and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters
    of a different word or phrase, typically using all
    the original letters exactly once.
    """
    if len(s) != len(t):
        return False

    s_freq = defaultdict(int)
    t_freq = defaultdict(int)

    for char1, char2 in zip(s, t):
        s_freq[char1] += 1
        t_freq[char2] += 1

    return s_freq == t_freq


@pytest.mark.parametrize(
    "s, t, expected",
    [("anagram", "nagaram", True), ("rat", "car", False)],
)
def test_is_anagram(s, t, expected):
    assert is_anagram(s, t) == expected
