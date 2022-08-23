import heapq

import pytest


def find_kth_smallest(lists, k):
    """
    Given ‘M’ sorted arrays,
    find the K’th smallest number among all the arrays.
    """
    min_heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i, 0))
    i = 0
    while min_heap:
        val, list_idx, idx = heapq.heappop(min_heap)

        if i == k - 1:
            return val

        if len(lists[list_idx]) > idx + 1:
            heapq.heappush(
                min_heap,
                (lists[list_idx][idx + 1], list_idx, idx + 1),
            )
        i += 1


@pytest.mark.parametrize(
    "lists, k, expected",
    [
        ([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5, 4),
        ([[5, 8, 9], [1, 7]], 3, 7),
    ],
)
def test_find_kth_smallest(lists, k, expected):
    assert find_kth_smallest(lists, k) == expected
