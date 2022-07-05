from typing import DefaultDict

import pytest


def find_word_concatenation(str, words):
    """
    Given a string and a list of words,
    find all the starting indices of substrings in the given string
    that are a concatenation of all the given words exactly once
    without any overlapping of words.

    It is given that all words are of the same length.
    """
    window_start = matches = 0
    k = len(words[0])
    freq_map = DefaultDict(int)
    res_indexes = []

    for w in words:
        freq_map[w] += 1

    for window_end in range(k - 1, len(str)):
        word = str[window_end - k + 1 : window_end + 1]
        if word in freq_map:
            freq_map[word] -= 1
            if freq_map[word] == 0:
                matches += 1

        if window_end - window_start + 1 > k * len(words):
            left_word = str[window_start : window_start + k]
            if left_word in freq_map:
                if freq_map[left_word] == 0:
                    matches -= 1
                freq_map[left_word] += 1
            window_start += 1

        if matches == len(freq_map):
            res_indexes.append(window_start)

    return res_indexes


@pytest.mark.parametrize(
    "str,words,expected",
    [
        ("catfoxcat", ["cat", "fox"], [0, 3]),
        ("catcatfoxfox", ["cat", "fox"], [3]),
        ("catcatcat", ["cat"], [0, 3, 6]),
        ("catcatcat", ["cat", "cat"], [0, 3]),
    ],
)
def test(str, words, expected):
    assert find_word_concatenation(str, words) == expected
