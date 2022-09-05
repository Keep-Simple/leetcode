import pytest


def solve_knapsack_top_down(profits, weights, capacity):
    """
    Given two integer arrays to represent weights and profits of ‘N’ items,
    we need to find a subset of these items which will give us maximum profit
    such that their cumulative weight is not more than a given number C.
    Each item can only be selected once, which means either
    we put an item in the knapsack or we skip it.

    TC: O(N*C), N=number of items, C=capacity
    SC: O(N*C)

    without memoization:
    TC: O(2^N)
    SC: 0(N) - for recursion stack
    """
    cache = [[-1 for _ in range(len(profits))] for _ in range(capacity + 1)]
    return _knapsack_recursive(profits, weights, capacity, 0, cache)


def _knapsack_recursive(profits, weights, capacity, idx, cache):
    if idx == len(profits):
        return 0

    if cache[capacity][idx] != -1:
        return cache[capacity][idx]

    without_curr = _knapsack_recursive(profits, weights, capacity, idx + 1, cache)
    with_curr = 0
    if weights[idx] <= capacity:
        with_curr = profits[idx] + _knapsack_recursive(
            profits, weights, capacity - weights[idx], idx + 1, cache
        )

    max_profit = max(with_curr, without_curr)

    cache[capacity][idx] = max_profit

    return max_profit


def solve_knapsack_bottom_up(profits, weights, capacity):
    """
    Same TC and SC as top_bottom approach
    """
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]
    for i in range(n):
        for c in range(capacity + 1):
            exclude = dp[i - 1][c]
            if weights[i] <= c:
                include = dp[i - 1][c - weights[i]] + profits[i]
                dp[i][c] = max(include, exclude)
            else:
                dp[i][c] = exclude
    # retrieve picked items, just a challange
    print_selected_elements(dp, weights, profits, capacity)
    return dp[-1][-1]


def print_selected_elements(dp, weights, profits, capacity):
    n = len(profits)
    total_profit = dp[-1][-1]
    for i in range(n - 1, 0, -1):
        if total_profit != dp[i - 1][capacity]:
            print(weights[i])
            capacity -= weights[i]
            total_profit -= profits[i]
    if total_profit != 0:
        print(weights[0])


def solve_knapsack_bottom_up_improved(profits, weights, capacity):
    """
    Same TC
    SC: O(C), keep last two rows for dp
    """
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for _ in range(capacity + 1)] for _ in range(2)]
    for i in range(n):
        for c in range(capacity + 1):
            exclude = dp[(i - 1) % 2][c]
            if weights[i] <= c:
                include = dp[(i - 1) % 2][c - weights[i]] + profits[i]
                dp[i % 2][c] = max(include, exclude)
            else:
                dp[i % 2][c] = exclude
    return dp[(n - 1) % 2][-1]


def solve_knapsack_bottom_up_improved_2(profits, weights, capacity):
    """
    Same TC
    SC: O(C), keep only one row with len == capacity + 1

    If you see closely, we need two values from the previous iteration:
    dp[c] and dp[c-weight[i]] (could be overriden in the current iteration, not good!)

    change inner loop to iterate in reverse direction, so dp[c-weight[i]]
    won't be overriden in the current iteration
    """
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [0 for _ in range(capacity + 1)]
    for i in range(n):
        for c in range(capacity, -1, -1):
            exclude = dp[c]
            if weights[i] <= c:
                include = dp[c - weights[i]] + profits[i]
                dp[c] = max(include, exclude)
            else:
                dp[c] = exclude
    return dp[-1]


@pytest.mark.parametrize(
    "profits, weights, capacity, expected",
    [
        ([1, 6, 10, 16], [1, 2, 3, 5], 5, 16),
        ([1, 6, 10, 16], [1, 2, 3, 5], 6, 17),
        ([1, 6, 10, 16], [1, 2, 3, 5], 7, 22),
    ],
)
def test_solve_knapsack(profits, weights, capacity, expected):
    assert solve_knapsack_top_down(profits, weights, capacity) == expected
    assert solve_knapsack_bottom_up(profits, weights, capacity) == expected
    assert solve_knapsack_bottom_up_improved(profits, weights, capacity) == expected
    assert solve_knapsack_bottom_up_improved_2(profits, weights, capacity) == expected
