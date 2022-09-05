import pytest


def can_partition(nums, sum):
    """
    Given a set of positive numbers,
    determine if a subset exists whose sum is equal to a given number ‘S’.

    TC: O(N*S)
    SC: O(S)
    """
    n = len(nums)
    dp = [False] * (sum + 1)
    dp[0] = True

    for i in range(n):
        for s in range(sum, -1, -1):
            exclude = dp[s]
            include = False
            if nums[i] <= s:
                include = dp[s - nums[i]]
            dp[s] = include or exclude

    return dp[-1]


def can_partition_2(nums, sum):
    """
    Less dp array writes
    """
    n = len(nums)
    dp = [False] * (sum + 1)
    dp[0] = True

    for i in range(n):
        for s in range(sum, -1, -1):
            # if dp[s]==true, this means we can get the sum 's' without num[i], hence we can move on to
            # the next number else we can include num[i] and see if we can find a subset to get the
            # remaining sum
            if not dp[s] and s >= nums[i]:
                dp[s] = dp[s - nums[i]]

    return dp[-1]


@pytest.mark.parametrize(
    "nums, sum, expected",
    [
        ([1, 2, 3, 7], 6, True),
        ([1, 2, 7, 1, 5], 10, True),
        ([1, 3, 4, 8], 6, False),
    ],
)
def test_can_partition(nums, sum, expected):
    assert can_partition(nums, sum) == expected
    assert can_partition_2(nums, sum) == expected
