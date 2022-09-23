import math

import pytest


def max_subarray_sum(nums):
    """
    Given an integer array nums,
    find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    A subarray is a contiguous part of an array.

    Solution:
        Dynamic Programming (Kadane's Algorithm)
        Calc max sum for each element (being the end of the subarray)
            by finding max(curr_element, dp[prev_idx] + curr_element), because dp[prev_idx] could be < 0
        Find max element (showing sum) in dp

        TC: O(N)
        SC: O(N)
    """
    n = len(nums)
    dp = [None] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

    return max(dp)


def max_subarray_sum_space_optimized(nums):
    n = len(nums)
    dp = ans = nums[0]
    for i in range(1, n):
        dp = max(dp + nums[i], nums[i])
        ans = max(ans, dp)

    return ans


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, -4, 3, -1, 2], 4),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ],
)
def test_max_subarray_sum(nums, expected):
    assert max_subarray_sum(nums) == expected
    assert max_subarray_sum_space_optimized(nums) == expected


def max_subarray_sum_non_negative(nums):
    """
    Given an integer array,
    find the largest sum of the subarray having only non-negative elements.
    """
    n = len(nums)
    dp = [None] * n
    dp[0] = nums[0] if nums[0] > 0 else 0
    for i in range(1, n):
        dp[i] = dp[i - 1] + nums[i] if nums[i] > 0 else 0

    return max(dp)


def max_subarray_sum_non_negative_space_optimized(nums):
    curr_max = 0
    global_max = -math.inf
    for num in nums:
        curr_max = curr_max + num if num > 0 else 0
        global_max = max(global_max, curr_max)

    return global_max


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 4, -3, 9, 5, -6], 14),
    ],
)
def test_max_subarray_sum_non_negative(nums, expected):
    assert max_subarray_sum_non_negative(nums) == expected
    assert max_subarray_sum_non_negative_space_optimized(nums) == expected
