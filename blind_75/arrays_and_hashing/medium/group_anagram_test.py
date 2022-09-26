from collections import defaultdict

import pytest


def group_anagrams(strs):
    """
    Given an array of strings strs, group the anagrams together.
    You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.
    """
    str_map = defaultdict(list)
    for str in strs:
        freq = [0] * 26
        for char in str:
            freq[ord(char) - ord("a")] += 1
        str_map[tuple(freq)].append(str)
    return str_map.values()


@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [
                ["eat", "tea", "ate"],
                ["tan", "nat"],
                ["bat"],
            ],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_group_anagrams(strs, expected):
    assert list(group_anagrams(strs)) == expected
