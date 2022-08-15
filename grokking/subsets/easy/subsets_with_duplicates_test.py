import pytest


def find_subsets(nums):
    """
    Given a set of numbers that might contain duplicates,
    find all of its distinct subsets.
    """
    subsets = [[]]
    nums.sort()
    prev_num = None
    end_idx = start_idx = 0
    for num in nums:
        n = len(subsets)
        if prev_num != num:
            end_idx = n
            start_idx = 0
        else:
            start_idx = n - end_idx
        prev_num = num

        for i in range(start_idx, n):
            subsets.append([*subsets[i], num])

    return subsets


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3, 3], [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]),
        (
            [1, 5, 3, 3],
            [
                [],
                [1],
                [5],
                [3],
                [1, 5],
                [1, 3],
                [3, 5],
                [1, 3, 5],
                [3, 3],
                [1, 3, 3],
                [3, 3, 5],
                [1, 3, 3, 5],
            ],
        ),
    ],
)
def test_find_subsets(nums, expected):
    res = find_subsets(nums)
    res.sort()
    expected.sort()
    assert res == expected
