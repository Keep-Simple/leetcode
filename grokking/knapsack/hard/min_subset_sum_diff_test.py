import pytest


def can_partition(nums):
    """
    Given a set of positive numbers,
    partition the set into two subsets with minimum
    difference between their subset sums.

    TC: O(N*(S/2))
    SC: O(S/2)
    """
    s = sum(nums)
    n = len(nums)
    half_s = s / 2
    dp = [half_s for _ in range(int(half_s + 1))]

    for i in range(n):
        for j in range(int(half_s), -1, -1):
            exclude = dp[j]
            if nums[i] <= j:
                include = dp[j - nums[i]] - nums[i]
                dp[j] = include if abs(include) <= abs(exclude) else exclude
            else:
                dp[j] = exclude
    return abs(dp[-1] * 2)


def can_partition_2(nums):
    """
    Provided solution with saving True/False instead of diff
    requires additional loop at the end to find closest
    """
    s = sum(nums)
    n = len(nums)
    dp = [[False for _ in range(int(s / 2) + 1)] for _ in range(n)]

    # populate the s=0 columns, as we can always form '0' sum with an empty set
    for i in range(0, n):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is equal to that number
    for j in range(0, int(s / 2) + 1):
        dp[0][j] = nums[0] == j

    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, int(s / 2) + 1):
            # if we can get the sum 's' without the number at index 'i'
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:
                # else include the number and see if we can find a subset to get the remaining sum
                dp[i][j] = dp[i - 1][j - nums[i]]

    sum1 = 0
    # find the largest index in the last row which is true
    for i in range(int(s / 2), -1, -1):
        if dp[n - 1][i]:
            sum1 = i
            break

    sum2 = s - sum1
    return abs(sum2 - sum1)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 7, 1, 5], 0),
        ([1, 2, 3, 9], 3),
        ([1, 3, 100, 4], 92),
    ],
)
def test_can_partition(nums, expected):
    assert can_partition(nums) == expected
    assert can_partition_2(nums) == expected
