import pytest


def count_subsets(nums, sum):
    """
    Given a set of positive numbers,
    find the total number of subsets whose sum is equal to a given number ‘S’.


    Solution:
    instead of keeping True/False, keep count
    to know how many possible ways there are
    to get the desired sum
    """
    n = len(nums)
    dp = [[0 for _ in range(sum + 1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1

    for s in range(sum + 1):
        if nums[0] == s:
            dp[0][s] = 1

    for i in range(1, n):
        for s in range(sum + 1):
            dp[i][s] = dp[i - 1][s]
            if nums[i] <= s:
                dp[i][s] += dp[i - 1][s - nums[i]]

    return dp[-1][-1]


def count_subsets_improved(nums, sum):
    """
    SC: O(S)
    """
    n = len(nums)
    dp = [0 for _ in range(sum + 1)]
    dp[0] = 1

    # for s in range(sum + 1):
    #     if nums[0] == s:
    #         dp[s] = 1

    for i in range(n):
        for s in range(sum, -1, -1):
            if nums[i] <= s:
                dp[s] += dp[s - nums[i]]

    return dp[-1]


@pytest.mark.parametrize(
    "nums, sum, expected",
    [
        ([1, 1, 2, 3], 4, 3),
        ([1, 2, 7, 1, 5], 9, 3),
        ([2, 7, 100, 5], 100, 1),
    ],
)
def test_count_subsets(nums, sum, expected):
    assert count_subsets(nums, sum) == expected
    assert count_subsets_improved(nums, sum) == expected
