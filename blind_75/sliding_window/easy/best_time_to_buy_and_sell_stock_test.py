import pytest


def max_profit(prices):
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy
    one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.

    Solution:
        TC: O(N)
        SC: O(1)
    Set to pointers to 0 and 1, update pointer 1 on each iteration
    update 0 only when prices[curr_idx] is lower than current
    Calculate max_profit on each step

    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/263197/Python-2-solutions%3A-Min-So-Far-Kadane's-Algorithm-with-Picture-O(1)-in-Space
    """
    # l - buy date
    # r - sell date
    l = 0
    max_profit = 0
    for r in range(1, len(prices)):
        # is profitable? => try to update max_profit
        if prices[l] < prices[r]:
            max_profit = max(max_profit, prices[r] - prices[l])
        else:
            l = r

    return max_profit


def max_profit_dp_kadanes(prices):
    """
    https://medium.com/geekculture/kadanes-algorithm-python-fccf1527eae6

    First map to max subarray sum,
    then solve using dp (Kadane's algo, optimized version with SC O(1), /leetcode/not_leetcode/max_subarray_sum_test.py)
    Then try to remove mapping array
    """
    n = len(prices)
    diffs = [None] * (n - 1)
    for i in range(n - 1):
        diffs[i] = prices[i + 1] - prices[i]

    curr_max = global_max = 0
    for diff in diffs:
        curr_max = max(diff, curr_max + diff)
        global_max = max(global_max, curr_max)

    return global_max


def max_profit_dp_kadanes_2(prices):
    """
    Removing mapping array (diffs)
    """
    n = len(prices)
    curr_max = global_max = 0
    for i in range(n - 1):
        profit = prices[i + 1] - prices[i]
        curr_max = max(curr_max + profit, profit)
        global_max = max(global_max, curr_max)

    return global_max


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 1, 2, 1, 0, 1, 2], 2),
    ],
)
def test_max_profit(prices, expected):
    assert max_profit(prices) == expected
    assert max_profit_dp_kadanes(prices) == expected
    assert max_profit_dp_kadanes_2(prices) == expected
