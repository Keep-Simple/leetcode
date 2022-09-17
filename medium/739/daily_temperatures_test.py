import math

import pytest


def daily_temperatures(temperatures):
    """
    Given an array of integers temperatures represents the daily temperatures,
    return an array answer such that answer[i] is the number of days
    you have to wait after the ith day to get a warmer temperature.
    If there is no future day for which this is possible,
    keep answer[i] == 0 instead.

    Solution:
        - iterating right to left and using stask
    """
    n = len(temperatures)
    stack = []
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()
        ans[i] = stack[-1] - i if stack else 0
        stack.append(i)

    return ans


def daily_temperatures_dp(temperatures):
    """
    From https://leetcode.com/problems/daily-temperatures/discuss/397728/Easy-Python-O(n)-time-O(1)-extra-space-beat-99.9
    """
    n = len(temperatures)
    right_max = -math.inf
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        curr_temp = temperatures[i]
        if right_max <= curr_temp:
            right_max = curr_temp
        else:
            days = 1
            while temperatures[i + days] <= curr_temp:
                days += ans[i + days]
            ans[i] = days

    return ans


def daily_temperatures_brute_force(temperatures):
    n = len(temperatures)
    ans = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[i] < temperatures[j]:
                ans[i] = j - i
                break
    return ans


@pytest.mark.parametrize(
    "temperatures, expected",
    [
        (
            [73, 74, 75, 71, 69, 72, 76, 73],
            [1, 1, 4, 2, 1, 1, 0, 0],
        ),
        (
            [30, 40, 50, 60],
            [1, 1, 1, 0],
        ),
        (
            [30, 60, 90],
            [1, 1, 0],
        ),
        (
            [89, 62, 70, 58, 47, 47, 46, 76, 100, 70],
            [8, 1, 5, 4, 3, 2, 1, 1, 0, 0],
        ),
    ],
)
def test_daily_temperatures(temperatures, expected):
    assert daily_temperatures_dp(temperatures) == expected
    assert daily_temperatures(temperatures) == expected
    assert daily_temperatures_brute_force(temperatures) == expected
