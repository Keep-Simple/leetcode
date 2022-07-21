import pytest


def find_first_k_missing_positive(nums, k):
    """
    Given an unsorted array containing numbers and a number ‘k’,
    find the first ‘k’ missing positive numbers in the array.
    """
    missing_nums = []
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if 0 <= j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    _nums = set()
    for i in range(n):
        if k == 0:
            return missing_nums
        if nums[i] - 1 != i:
            missing_nums.append(i + 1)
            _nums.add(nums[i])
            k -= 1
    i = n
    while k > 0:
        i += 1
        if i not in _nums:
            missing_nums.append(i)
            k -= 1
    return missing_nums


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, -1, 4, 5, 5], 3, [1, 2, 6]),
        ([2, 3, 4], 3, [1, 5, 6]),
        ([-2, -3, 4], 2, [1, 2]),
    ],
)
def test_find_first_k_missing_positive(nums, k, expected):
    assert find_first_k_missing_positive(nums, k) == expected
