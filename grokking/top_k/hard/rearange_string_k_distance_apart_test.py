import heapq
from collections import deque

import pytest


def reorganize_string(str, k):
    """
    Given a string and a number ‘K’,
    find if the string can be rearranged such that
    the same characters are at least ‘K’ distance apart from each other.
    """
    freq_map = {}
    for char in str:
        freq_map[char] = freq_map.get(char, 0) + 1

    max_heap = []
    queue = deque()
    ans = []

    for char, freq in freq_map.items():
        heapq.heappush(max_heap, (-freq, char))

    i = 0
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        freq = -freq - 1
        ans.append(char)

        if i >= k - 1 and queue:
            heapq.heappush(max_heap, queue.popleft())

        if freq > 0:
            queue.append((-freq, char))
        i += 1

    return "".join(ans) if len(ans) == len(str) else ""


@pytest.mark.parametrize(
    "str,k, expected",
    [
        ("mmpp", 2, "mpmp"),
        ("Programming", 3, "gmrPagimnor"),
        ("aab", 2, "aba"),
        ("aapa", 3, ""),
        ("abc", 1, "abc"),
    ],
)
def test_reorganize_string(str, k, expected):
    assert reorganize_string(str, k) == expected
