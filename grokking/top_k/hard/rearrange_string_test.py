import heapq
from collections import defaultdict

import pytest


def rearrange_string(str):
    """
    Given a string, find if its letters can be rearranged
    in such a way that no two same characters come next to each other.
    """
    # build freq_map
    # insert most frequent chars first to get more success chances
    # return prev element to the max_heap in each next step
    freq_map = defaultdict(int)

    for char in str:
        freq_map[char] += 1

    max_heap = []

    for char, freq in freq_map.items():
        heapq.heappush(max_heap, (-freq, char))

    prev_char, prev_freq = None, 0
    ans = []

    while max_heap:
        freq, char = heapq.heappop(max_heap)

        if prev_char and prev_freq > 0:
            heapq.heappush(max_heap, (-prev_freq, prev_char))

        ans.append(char)
        prev_char = char
        prev_freq = -freq - 1

    return "".join(ans) if len(ans) == len(str) else ""


@pytest.mark.parametrize(
    "str, expected",
    [
        ("aappp", "papap"),
        ("Programming", "gmrPagimnor"),  # or rgmrgmPiano, etc
        ("aapa", ""),
    ],
)
def test_rearrange_string(str, expected):
    assert rearrange_string(str) == expected
