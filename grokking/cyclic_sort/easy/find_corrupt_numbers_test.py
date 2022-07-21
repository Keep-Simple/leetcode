import pytest


def find_corrupt_numbers(nums):
    """
    We are given an unsorted array containing ‘n’ numbers
    taken from the range 1 to ‘n’.
    The array originally contained all the numbers from 1 to ‘n’,
    but due to a data error, one of the numbers got duplicated which
    also resulted in one number going missing.
    Find both these numbers.
    """
    i = 0
    while i < len(nums):
        j = nums[i] - 1

        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] - 1 != i:
            return [nums[i], i + 1]


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 1, 2, 5, 2], [2, 4]),
        ([3, 1, 2, 3, 6, 4], [3, 5]),
    ],
)
def test_find_corrupt_numbers(nums, expected):
    assert find_corrupt_numbers(nums) == expected
