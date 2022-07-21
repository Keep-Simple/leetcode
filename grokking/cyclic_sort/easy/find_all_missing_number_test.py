import pytest


def find_missing_numbers(nums):
    """
    We are given an unsorted array containing numbers
    taken from the range 1 to ‘n’.
    The array can have duplicates, which means some numbers will be missing.
    Find all those missing numbers.
    """
    missing_numbers = []
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] - 1 != i:
            missing_numbers.append(i + 1)
    return missing_numbers


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 1, 8, 2, 3, 5, 1], [4, 6, 7]),
        ([2, 4, 1, 2], [3]),
        ([2, 3, 2, 1], [4]),
    ],
)
def test_find_missing_numbers(nums, expected):
    assert find_missing_numbers(nums) == expected
