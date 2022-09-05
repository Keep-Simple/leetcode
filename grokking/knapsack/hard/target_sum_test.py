import pytest


def find_target_subsets(nums, s):
    """
    You are given a set of positive numbers and a target sum ‘S’.
    Each number should be assigned either a ‘+’ or ‘-’ sign.
    We need to find the total ways to assign symbols
    to make the sum of the numbers equal to the target ‘S’
    """

    def _recursive(nums, s, idx):
        if idx == len(nums):
            return 1 if s == 0 else 0
        with_plus = _recursive(nums, s - nums[idx], idx + 1)
        with_minus = _recursive(nums, s + nums[idx], idx + 1)
        res = with_plus + with_minus
        return res

    return _recursive(nums, s, 0)


def find_target_subsets_2(nums, s):
    """
    Bottom-up approach

    Assume that s is a positive integer
    if it's negative the answer would be the same
    just invert + to - and - to +

    Start with all +, and replace with - where possible
    capacity is sum(nums) - s


    It's actually the same as solution 4, but instead of
    math equations, I came up with a solution using bare logic
    """
    n = len(nums)
    nums_sum = sum(nums)
    diff = nums_sum - s
    dp = [0] * (diff + 1)
    dp[0] = 1

    for i in range(n):
        for c in range(diff, -1, -1):
            if nums[i] * 2 <= c:
                dp[c] += dp[c - nums[i] * 2]

    return dp[-1]


"""
Solutions 3 and 4 are based on the same math logic
S1 - S2 = s, where s is desired number == subsets sum difference in our case
S1 + S2 = nums_sum, where S1 and S2 is sum of two subsets

it's linear eq. system, we can add or substract them
Add:
    2*S1 = s + nums_sum
    S1 = (s+nums_sum)/2, we need to find subset with sum S1
Substract:
    2S2 = nums_sum - s
    S2 = (nums_sum - s)/2, we need to find subset with sum S2

Depending on nums_sum and s values range we should peek on add/substract
(Aiming to minimize range of the subset sum to reduce TC & SC)
"""


def find_target_subsets_3(nums, s):
    nums_sum = sum(nums)
    if nums_sum < s or (s + nums_sum) % 2 == 1:
        return 0
    return count_subsets(nums, (s + nums_sum) // 2)


def find_target_subsets_4(nums, s):
    nums_sum = sum(nums)
    diff = nums_sum - s
    if nums_sum < s or diff % 2 == 1:
        return 0
    return count_subsets(nums, diff // 2)


def count_subsets(nums, s):
    n = len(nums)
    dp = [0] * (s + 1)
    dp[0] = 1

    """
    Don't need a separate loop to fill first iteration
    dp[0] = 1 is set
    and if nums[0] is equal to i => dp[i] = dp[i-nums[i]] = dp[0]
    """
    # dp = [1]
    # # fill first iteration
    # # with only one number, we can form a subset
    # # only when the required sum is equal to the number
    # for i in range(1, s + 1):
    #     dp.append(1 if nums[0] == i else 0)

    for i in range(n):
        for c in range(s, -1, -1):
            if nums[i] <= c:
                dp[c] += dp[c - nums[i]]

    return dp[-1]


@pytest.mark.parametrize(
    "nums,s, expected",
    [
        ([1, 1, 2, 3], 1, 3),
        ([1, 2, 7, 1], 9, 2),
        ([1, 2, 7, 1], 9, 2),
    ],
)
def test_find_target_subsets(nums, s, expected):
    assert find_target_subsets(nums, s) == expected
    assert find_target_subsets_2(nums, s) == expected
    assert find_target_subsets_3(nums, s) == expected
    assert find_target_subsets_4(nums, s) == expected
