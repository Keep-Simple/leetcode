import heapq
from collections import defaultdict

import pytest


def find_maximum_distinct_elements(nums, k):
    """
    Given an array of numbers and a number ‘K’,
    we need to remove ‘K’ numbers from the array such that
    we are left with maximum distinct numbers.
    """
    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1

    ans = 0
    min_heap = []
    for num, freq in freq_map.items():
        if freq == 1:
            ans += 1
        else:
            item = (freq, num)
            if len(min_heap) < k:
                heapq.heappush(min_heap, item)
            elif min_heap[0] > item:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, item)

    while min_heap and k > 0:
        freq, num = heapq.heappop(min_heap)
        if k >= freq - 1:
            ans += 1
            k -= freq - 1
        else:
            k = 0

    return ans - k


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([7, 3, 5, 8, 5, 3, 3], 2, 3),
        ([3, 5, 12, 11, 12], 3, 2),
        ([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2, 3),
    ],
)
def test_find_maximum_distinct_elements(nums, k, expected):
    assert find_maximum_distinct_elements(nums, k) == expected
