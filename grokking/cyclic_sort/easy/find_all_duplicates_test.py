import pytest


def find_all_duplicates(nums):
    """
    We are given an unsorted array containing n numbers taken
    from the range 1 to n.
    The array has some numbers appearing twice,
    find all these duplicate numbers using constant space.
    """
    i = 0
    duplicates = []

    while i < len(nums):
        j = nums[i] - 1

        if nums[j] != nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
        else:
            if j != i:
                duplicates.append(nums[i])
            i += 1
    return duplicates


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 4, 4, 5, 5], [5, 4]),
        ([5, 4, 7, 2, 3, 5, 3], [3, 5]),
    ],
)
def test_find_all_duplicates(nums, expected):
    assert find_all_duplicates(nums) == expected
