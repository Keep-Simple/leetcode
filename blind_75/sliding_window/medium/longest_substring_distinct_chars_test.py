import pytest


def length_of_longest_substring(s):
    """
    Given a string s,
    find the length of the longest substring without repeating characters.
    """
    char_map = {}
    window_start = 0
    max_len = 0
    for window_end in range(len(s)):
        char = s[window_end]
        if char in char_map and window_start <= char_map[char]:
            window_start = char_map[char] + 1
        char_map[char] = window_end
        max_len = max(max_len, window_end - window_start + 1)
    return max_len


def alternative(s):
    """
    WTF solution - https://www.youtube.com/watch?v=wiGpQwVHdE0
    Looks like python maintaines insert order for set somehow
    A lot of add/remove operations on set, better memory though
    Prefer the 1st solution
    """
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("abba", 2),
    ],
)
def test_length_of_longest_substring(s, expected):
    assert length_of_longest_substring(s) == expected
    assert alternative(s) == expected
