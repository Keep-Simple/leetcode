import pytest


def contains_duplicate(nums):
    """
    Given an integer array nums,
    return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    """
    nums_set = set()
    for i in range(len(nums)):
        if nums[i] in nums_set:
            return True
        nums_set.add(nums[i])

    return False


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_contains_duplicate(nums, expected):
    assert contains_duplicate(nums) == expected
