import pytest


def find_subsets(nums):
    """
    Given a set with DISTINCT elements,
    find all of its distinct subsets.

    O(N * 2^N): Each num double sets amount(O(2^N)), to create new set O(N)
    """
    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            subsets.append([*subsets[i], num])
    return subsets


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3], [[], [1], [3], [1, 3]]),
        ([1, 5, 3], [[], [1], [5], [3], [1, 5], [1, 3], [5, 3], [1, 5, 3]]),
    ],
)
def test_find_subsets(nums, expected):
    res = find_subsets(nums)
    res.sort()
    expected.sort()
    assert res == expected
