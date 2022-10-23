import pytest


def climb_stairs(n):
    """
    https://leetcode.com/problems/climbing-stairs/

    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?

    Solution:
        c(i)=c(i-1)+c(i-2), the ways count on current stair is equal to sum of prev and prevprev
        c(1) = 1
        c(2) = 2

    Start from the bottom, calculating the next element from previous 2
    decrement n till we find the value
    """
    prev = [1, 2]
    n -= 1

    while n > 1:
        prev[1], prev[0] = prev[0] + prev[1], prev[1]
        n -= 1

    return prev[n]


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 2),  # 1 step + 1 step, 2 steps
        (3, 3),  # 1 + 1 + 1, 1 + 2, 2 + 1
    ],
)
def test_climb_stairs(n, expected):
    assert climb_stairs(n) == expected
