import pytest


def find_first_smallest_missing_positive(nums):
    """
    Given an unsorted array containing numbers,
    find the smallest missing positive number in it.
    Note: Positive numbers start from ‘1’.
    """
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if 0 <= j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] - 1 != i:
            return i + 1

    return n + 1


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-3, 1, 5, 4, 2], 3),
        ([3, -2, 0, 1, 2], 4),
        ([3, 2, 5, 1], 4),
    ],
)
def test_find_first_smallest_missing_positive(nums, expected):
    assert find_first_smallest_missing_positive(nums) == expected
