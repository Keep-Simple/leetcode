import math
from heapq import heappop, heappush

import pytest


def find_smallest_range(lists):
    """
    Given ‘M’ sorted arrays,
    find the smallest range that includes
    at least one number from each of the ‘M’ lists.


    TC - O(N*log(M)), where N is count of all elements from lists
    SC - O(M), for heap
    """
    n = len(lists)
    min_heap = []
    max_el = -math.inf

    for i in range(n):
        if lists[i]:
            heappush(min_heap, (lists[i][0], i, 0))
            max_el = max(max_el, lists[i][0])

    range_start = range_end = None

    while len(min_heap) == n:
        val, list_idx, idx = heappop(min_heap)

        if range_start is None or max_el - val < range_end - range_start:
            range_start = val
            range_end = max_el

        if idx + 1 < len(lists[list_idx]):
            new_el = lists[list_idx][idx + 1]
            max_el = max(max_el, new_el)
            heappush(min_heap, (new_el, list_idx, idx + 1))

    return [range_start, range_end]


@pytest.mark.parametrize(
    "lists, expected",
    [
        ([[1, 5, 8], [4, 12], [7, 8, 10]], [4, 7]),
        ([[1, 9], [4, 12], [7, 10, 16]], [9, 12]),
    ],
)
def test_find_smallest_range(lists, expected):
    assert find_smallest_range(lists) == expected
