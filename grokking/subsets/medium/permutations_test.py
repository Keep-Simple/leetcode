from collections import deque

import pytest


def find_permutations(nums):
    nums_length = len(nums)
    result = []
    permutations = deque([[]])
    for num in nums:
        # we will take all existing permutations
        # and add the current number to create new permutations
        for _ in range(len(permutations)):
            old_permutation = permutations.popleft()
            # create a new permutation
            # by adding the current number at every position
            for j in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(j, num)
                if len(new_permutation) == nums_length:
                    result.append(new_permutation)
                else:
                    permutations.append(new_permutation)

    return result


def find_permutations_2(nums):
    """
    Given a set of distinct numbers,
    find all of its permutations.
    """
    ans = [[]]
    for num in nums:
        new_ans = []
        for j in range(len(ans)):
            for i in range(len(ans[j]) + 1):
                copy = ans[j].copy()
                copy.insert(i, num)
                new_ans.append(copy)
        ans = new_ans
    return ans


@pytest.mark.parametrize(
    "nums, expected",
    [
        (
            [1, 3, 5],
            [
                [1, 3, 5],
                [1, 5, 3],
                [3, 1, 5],
                [3, 5, 1],
                [5, 1, 3],
                [5, 3, 1],
            ],
        ),
    ],
)
def test_find_permutations(nums, expected):
    res = find_permutations(nums)
    res.sort()
    expected.sort()
    assert res == expected

    res = find_permutations_2(nums)
    res.sort()
    expected.sort()
    assert res == expected
