import pytest


def cyclic_sort(nums):
    """
    Write a function to sort the objects in-place on their creation
    sequence number (from 1 to n) in O(n) and without using any extra space
    """
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 1, 5, 4, 2], [1, 2, 3, 4, 5]),
        ([2, 6, 4, 3, 1, 5], [1, 2, 3, 4, 5, 6]),
        ([1, 5, 6, 4, 3, 2], [1, 2, 3, 4, 5, 6]),
    ],
)
def test_cyclic_sort(nums, expected):
    assert cyclic_sort(nums) == expected
