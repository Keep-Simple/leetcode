from typing import DefaultDict

import pytest


def length_of_longest_substring(str, k):
    """
    - iterate through string add one letter at a time to the window
    - keep track of the max repeating letter in the current window
    - if max_repeat_count + k (chars we can replace) < window_size
        => we shrink window by one (move it 1 cell forward)
    """
    window_start = max_size = max_repeat_count = 0
    freq_map = DefaultDict(int)

    for window_end in range(len(str)):
        char = str[window_end]
        freq_map[char] += 1
        max_repeat_count = max(max_repeat_count, freq_map[char])

        if window_end - window_start + 1 > max_repeat_count + k:
            # shrink
            freq_map[str[window_start]] -= 1
            window_start += 1

        max_size = max(max_size, window_end - window_start + 1)

    return max_size


def length_of_longest_ones(arr, k):
    window_start = max_size = max_ones = 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones += 1

        if window_end - window_start + 1 > max_ones + k:
            if arr[window_start] == 1:
                max_ones -= 1
            window_start += 1

        max_size = max(max_size, window_end - window_start + 1)

    return max_size


@pytest.mark.parametrize(
    "str,k,expected",
    [
        ("aabccbb", 2, 5),
        ("abbcb", 1, 4),
        ("abccde", 1, 3),
    ],
)
def test(str, k, expected):
    assert length_of_longest_substring(str, k) == expected


@pytest.mark.parametrize(
    "arr,k,expected",
    [
        ([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2, 6),
        ([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3, 9),
    ],
)
def test_2(arr, k, expected):
    assert length_of_longest_ones(arr, k) == expected
