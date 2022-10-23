import pytest


def pacific_atlantic(heights):
    """
    https://leetcode.com/problems/pacific-atlantic-water-flow/

    There is an m x n rectangular island
    that borders both the Pacific Ocean and Atlantic Ocean.
    The Pacific Ocean touches the island's left and top edges,
    and the Atlantic Ocean touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells.
    You are given an m x n integer matrix heights where heights[r][c]
    represents the height above sea level of the cell at coordinate (r, c).

    The island receives a lot of rain,
    and the rain water can flow to neighboring cells directly
    north, south, east, and west if the neighboring cell's
    height is less than or equal to the current cell's height.
    Water can flow from any cell adjacent to an ocean into the ocean.

    Return a 2D list of grid coordinates result where result[i] = [ri, ci]
    denotes that rain water can flow from cell (ri, ci)
    to both the Pacific and Atlantic oceans.

    Solution:
        Cells adjacent to:
        - Pacific Ocean [0][...] + [...][0]
        - Atlantic Ocean [m][...] + [...][n]

        For EACH cell start a dfs traversal,
        if it reaches both oceans add to the answer

        TC: O((n*m)^2)
        SC: O(1)
    """
    ans = []
    m = len(heights)
    n = len(heights[0])
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def dfs(y, x, oceans):
        cell = heights[y][x]
        heights[y][x] = "#"

        if (y == 0 or x == 0) and 0 not in oceans:
            oceans.append(0)

        if (y == m - 1 or x == n - 1) and 1 not in oceans:
            oceans.append(1)

        if len(oceans) == 2:
            heights[y][x] = cell
            return True

        for delta_y, delta_x in moves:
            new_y = y + delta_y
            new_x = x + delta_x
            if (
                not (0 <= new_x < n and 0 <= new_y < m)
                or heights[new_y][new_x] == "#"
                or cell < heights[new_y][new_x]
            ):
                continue
            if dfs(new_y, new_x, oceans):
                heights[y][x] = cell
                return True

        heights[y][x] = cell

    for y in range(m):
        for x in range(n):
            oceans = []
            if dfs(y, x, oceans):
                ans.append([y, x])

    return ans


def pacific_atlantic_2(heights):
    """
    Solution O(n*m) solution
    Start from the end, take cells adjacent to pacific and atlantic
    ocean and dfs with all possible movements (top, right, bottom, left)
    Store visited cells for each ocean separatly (also use it to prevent visiting the same cell twice)
    Finally find the intersection of visited cells of 2 oceans

    Drawbacks:
        Additional SC - O(n*m)
    """
    m = len(heights)
    n = len(heights[0])
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    pacific_visited = set()
    atlantic_visited = set()

    def dfs(y, x, visited):
        cords = (y, x)
        if cords in visited:
            return
        visited.add(cords)
        cell = heights[y][x]

        for delta_y, delta_x in moves:
            new_x = x + delta_x
            new_y = y + delta_y
            if 0 <= new_x < n and 0 <= new_y < m and heights[new_y][new_x] >= cell:
                dfs(new_y, new_x, visited)

        heights[y][x] = cell

    y = 0
    for x in range(n):
        dfs(y, x, pacific_visited)
    x = 0
    for y in range(m):
        dfs(y, x, pacific_visited)

    y = m - 1
    for x in range(n):
        dfs(y, x, atlantic_visited)
    x = n - 1
    for y in range(m):
        dfs(y, x, atlantic_visited)

    return pacific_visited.intersection(atlantic_visited)


@pytest.mark.parametrize(
    "heights, expected",
    [
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [
                [0, 4],
                [1, 3],
                [1, 4],
                [2, 2],
                [3, 0],
                [3, 1],
                [4, 0],
            ],
        ),
        ([[1]], [[0, 0]]),
    ],
)
def test_pacific_atlantic(heights, expected):
    assert sorted(pacific_atlantic(heights)) == sorted(expected)
    assert sorted(pacific_atlantic_2(heights)) == sorted(
        map(lambda e: (e[0], e[1]), expected)
    )
