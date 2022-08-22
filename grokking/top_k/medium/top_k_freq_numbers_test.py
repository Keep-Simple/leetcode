import heapq
from collections import defaultdict

import pytest


def find_k_frequent_numbers(nums, k):
    """
    Given an unsorted array of numbers,
    find the top ‘K’ frequently occurring numbers in it.
    """
    # can be implemented like LRU cache
    # (using OrderedDict or HashMap + LinkedList)
    # Time Complexite will improve from O(n+n*logk) -> O(n)
    freq_map = defaultdict(int)

    min_heap = []

    for num in nums:
        freq_map[num] += 1

    for key, freq in freq_map.items():
        item = (freq, key)
        if len(min_heap) < k:
            heapq.heappush(min_heap, item)
        elif min_heap[0] < item:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, item)

    return list(map(lambda el: el[1], min_heap))


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 3, 5, 12, 11, 12, 11], 2, [11, 12]),
        ([5, 12, 11, 3, 11], 2, [12, 11]),  # or [11, 5] or [11, 3]
    ],
)
def test_find_k_frequent_numbers(nums, k, expected):
    assert find_k_frequent_numbers(nums, k) == expected
