import pytest


def find_missing_number(nums):
    """
    We are given an array containing n distinct numbers
    taken from the range 0 to n.
    Since the array has only n numbers out of the total n+1 numbers,
    find the missing number.
    """
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    # find the first number missing from its index
    # that will be our required number
    for i in range(n):
        if nums[i] != i:
            return i

    return n


@pytest.mark.parametrize(
    "nums, expected",
    [([4, 0, 3, 1], 2), ([8, 3, 5, 2, 4, 6, 0, 1], 7), ([0, 1, 2, 3], 4)],
)
def test_find_missing_number(nums, expected):
    assert find_missing_number(nums) == expected
