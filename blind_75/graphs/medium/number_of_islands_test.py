import pytest


def num_of_islands(grid):
    """
    https://leetcode.com/problems/number-of-islands/

    Given an m x n 2D binary grid
    which represents a map of '1's (land) and '0's (water),
    return the number of islands.

    An island is surrounded by water and is formed by
    connecting adjacent lands horizontally or vertically.
    You may assume all four edges of the grid are all surrounded by water.

    Solution:
        Go through the grid,
        if we find 1 (land), increment islands by 1
        and recursively (dfs) mark all neighboring land as visited ("#")

    TC:
        m*n - going through the grid
        we are visiting each land only once, and skip water and visited

        O(m*n)
    """
    m = len(grid)
    n = len(grid[0])
    islands = 0
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def dfs(y, x):
        if not (0 <= x < n and 0 <= y < m) or grid[y][x] != "1":
            return

        grid[y][x] = "#"

        for y_delta, x_delta in moves:
            dfs(y + y_delta, x + x_delta)

    for y in range(m):
        for x in range(n):
            if grid[y][x] == "1":
                islands += 1
                dfs(y, x)

    return islands


@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
    ],
)
def test_num_of_islands(grid, expected):
    assert num_of_islands(grid) == expected
