import pytest


def can_partition(nums):
    """
    Given a set of positive numbers,
    find if we can partition it into two subsets
    such that the sum of elements in both subsets is equal.

    we want to minimize diff between subsets sum
    iterating through nums, we can send num to subset 1 or subset 2
    """
    nums_sum = sum(nums)
    if nums_sum % 2 != 0:
        return False
    subset_sum = nums_sum // 2
    dp = [[-1 for _ in range(subset_sum + 1)] for _ in range(len(nums))]
    return _can_partition_recursive(nums, subset_sum, 0, dp) == 1


def _can_partition_recursive(nums, capacity, idx, dp):
    if capacity == 0:
        return 1

    n = len(nums)
    if n == 0 or idx == n:
        return 0

    if dp[idx][capacity] != -1:
        return dp[idx][capacity]

    include = 0
    if nums[idx] <= capacity:
        include = _can_partition_recursive(nums, capacity - nums[idx], idx + 1, dp)
    exclude = _can_partition_recursive(nums, capacity, idx + 1, dp)
    res = max(exclude, include)
    dp[idx][capacity] = res
    return res


def can_partition_bottom_up(nums):
    nums_sum = sum(nums)
    n = len(nums)
    if nums_sum % 2 != 0:
        return False
    subset_sum = nums_sum // 2
    dp = [[False for _ in range(subset_sum + 1)] for _ in range(2)]

    for i in range(len(dp)):
        dp[i][0] = True

    for i in range(n):
        for j in range(subset_sum + 1):
            exclude = dp[(i - 1) % 2][j]
            include = False
            if j >= nums[i]:
                include = dp[(i - 1) % 2][j - nums[i]]
            dp[i % 2][j] = exclude or include

    return dp[(n - 1) % 2][-1]


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], True),  # 1,4 and 2,3
        ([1, 1, 3, 4, 7], True),  # 1,3,4 and 1,7
        ([2, 3, 4, 6], False),
        ([1, 2, 3, 8], False),
    ],
)
def test_can_partition(nums, expected):
    assert can_partition(nums) == expected
    assert can_partition_bottom_up(nums) == expected
