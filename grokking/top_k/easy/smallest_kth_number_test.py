import heapq

import pytest


class MaxHeap:
    def __init__(self):
        self.data = []

    def push(self, element):
        heapq.heappush(self.data, -element)

    def pop(self):
        heapq.heappop(self.data)

    def peek(self):
        return -self.data[0] if self.data else None

    def __len__(self):
        return len(self.data)


def find_kth_smallest_number(nums, k):
    """
    Given an unsorted array of numbers,
    find Kth smallest number in it.

    Please note that it is the Kth smallest number in the sorted order,
    not the Kth distinct element
    """
    max_heap = MaxHeap()

    for i in range(k):
        max_heap.push(nums[i])

    for i in range(k, len(nums)):
        if max_heap.peek() > nums[i]:
            max_heap.pop()
            max_heap.push(nums[i])

    return max_heap.peek()


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 5, 12, 2, 11, 5], 3, 5),
        ([1, 5, 12, 2, 11, 5], 4, 5),
        ([5, 12, 11, -1, 12], 3, 11),
    ],
)
def test_find_k_smallest_number(nums, k, expected):
    assert find_kth_smallest_number(nums, k) == expected
