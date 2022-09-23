from collections import defaultdict

import pytest


def char_replacement(s, k):
    """
    You are given a string s and an integer k.
    You can choose any character of the string and change it to any other uppercase English character.
    You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations.

    Solution:
        - Start a sliding window and keep freq_map for characters
        - Know the max_freq of some char in the current window (actually it's maximum freq from all prev window states)
        - If max_freq + k < window_size => shrink window by 1
          Else update max_len
          (there is no point in shrinking more, as we want the longest substring)
        -
    """
    freq_map = defaultdict(int)
    window_start = max_len = 0
    max_freq = 0
    for window_end in range(len(s)):
        char = s[window_end]
        freq_map[char] += 1
        max_freq = max(max_freq, freq_map[char])
        if max_freq + k < window_end - window_start + 1:
            freq_map[s[window_start]] -= 1
            window_start += 1
        else:
            max_len = max(max_len, window_end - window_start + 1)

    return max_len


def char_replacement_simple(s, k):
    # max 26 keys (letters from A-Z)
    """
    Solution:
        - sliding window with condition window_size < max_freq + k
        - it's the same as previous solution, but
          previous solution optimized max(freq_map.values()) lookup
          by keeping max_freq in increase only state (there is no point to decrease to find the answer, because we need the longest substring)
          in other words once we never shrink window, only keeping the same or growing
    Also while can be changed to if for the same reason
    """
    freq_map = defaultdict(int)
    window_start = max_len = 0
    for window_end in range(len(s)):
        freq_map[s[window_end]] += 1
        while window_end - window_start + 1 > max(freq_map.values()) + k:
            freq_map[s[window_start]] -= 1
            window_start += 1
        max_len = max(max_len, window_end - window_start + 1)

    return max_len


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("ABAA", 0, 2),
    ],
)
def test_char_replacement(s, k, expected):
    assert char_replacement(s, k) == expected
    assert char_replacement_simple(s, k) == expected
