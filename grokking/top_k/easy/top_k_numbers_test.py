import heapq

import pytest


def find_k_largest_numbers(nums, k):
    """
    Given an unsorted array of numbers,
    find the ‘K’ largest numbers in it.
    """
    min_heap = []
    for i in range(k):
        heapq.heappush(min_heap, nums[i])
    for i in range(k, len(nums)):
        if min_heap[0] < nums[i]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, nums[i])
    return min_heap


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, 1, 5, 12, 2, 11], 3, [5, 12, 11]),
        ([5, 12, 11, -1, 12], 3, [11, 12, 12]),
    ],
)
def test_find_k_largest_numbers(nums, k, expected):
    assert find_k_largest_numbers(nums, k) == expected
