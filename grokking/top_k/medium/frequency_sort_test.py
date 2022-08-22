import heapq
from collections import defaultdict

import pytest


def sort_character_by_frequency(str):
    """
    Given a string,
    sort it based on the decreasing frequency of its characters.
    """
    freq_map = defaultdict(int)
    for char in str:
        freq_map[char] += 1

    min_heap = []

    for char, freq in freq_map.items():
        item = (freq, char)
        heapq.heappush(min_heap, item)

    ans = []

    while min_heap:
        freq, char = heapq.heappop(min_heap)
        ans.extend([char] * freq)
    ans.reverse()

    return "".join(ans)


@pytest.mark.parametrize(
    "str, expected",
    [
        ("Programming", "rrmmggoniaP"),
        ("abcbab", "bbbaac"),
    ],
)
def test_sort_character_by_frequency(str, expected):
    assert sort_character_by_frequency(str) == expected
