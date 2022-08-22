import heapq

import pytest


def find_sum_of_elements(nums, k1, k2):
    """
    Given an array, find the sum of all numbers
    between the K1’th and K2’th smallest elements of that array.
    """
    max_heap = []

    for num in nums:
        if len(max_heap) < k2 - 1:
            heapq.heappush(max_heap, -num)
        elif -max_heap[0] > num:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -num)

    sum = 0
    for _ in range(k2 - k1 - 1):
        sum += -heapq.heappop(max_heap)
    return sum


@pytest.mark.parametrize(
    "nums, k1, k2, expected",
    [
        ([1, 3, 12, 5, 15, 11], 3, 6, 23),
        ([3, 5, 8, 7], 1, 4, 12),
    ],
)
def test_find_sum_of_elements(nums, k1, k2, expected):
    assert find_sum_of_elements(nums, k1, k2) == expected
