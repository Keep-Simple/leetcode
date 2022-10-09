import pytest


def exist(board, word):
    """
    Given an m x n grid of characters board and a string word,
    return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once.
    """
    # top, right, bottom, left
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    m = len(board)  # y
    n = len(board[0])  # x

    def dfs(x, y, char_idx):
        if not (0 <= x < n and 0 <= y < m):
            return False

        curr_char = board[y][x]
        char = word[char_idx]

        if curr_char == "#" or curr_char != char:
            return False

        if char_idx == len(word) - 1:
            return True

        board[y][x] = "#"  # mark visited

        visit_neighbours_res = False
        for delta_y, delta_x in moves:
            if dfs(x + delta_x, y + delta_y, char_idx + 1):
                visit_neighbours_res = True
                break

        board[y][x] = curr_char  # mark unvisited

        return visit_neighbours_res

    for y in range(m):
        for x in range(n):
            if dfs(x, y, 0):
                return True

    return False


@pytest.mark.parametrize(
    "board, word, expected",
    [
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCCED",
            True,
        ),
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "SEE",
            True,
        ),
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCB",
            False,
        ),
        (
            [
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "B"],
                ["A", "A", "A", "A", "B", "A"],
            ],
            "AAAAAAAAAAAAABB",
            False,
        ),
    ],
)
def test_exist(board, word, expected):
    assert exist(board, word) == expected
