import pytest


def find_duplicate(nums):
    """
    We are given an unsorted array containing ‘n+1’
    numbers taken from the range 1 to ‘n’.
    The array has only one duplicate but it can be repeated multiple times.
    Find that duplicate number without using any extra space.
    You are, however, allowed to modify the input array.

    Can also solve it without modifying the input array
    with fast&slow pointers (finding the cycle start)
    """
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[j] != nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
        else:
            if i != j:
                return nums[i]
            i += 1

    return -1


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 4, 4, 3, 2], 4),
        ([2, 1, 3, 3, 5, 4], 3),
        ([2, 4, 1, 4, 4], 4),
    ],
)
def test_find_duplicate(nums, expected):
    assert find_duplicate(nums) == expected
