import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )


def count_unique_trees(n):
    """
    Given a number ‘n’,
    write a function to return the count of structurally
    unique Binary Search Trees (BST) that can store values 1 to ‘n’.
    """
    if n <= 0:
        return 0

    return _count_recursive(1, n)


cache = {}


def _count_recursive(start, end):
    if end < start:
        return 1
    key = (start, end)
    if key in cache:
        return cache[key]

    result = 0
    for i in range(start, end + 1):
        left = _count_recursive(start, i - 1)
        right = _count_recursive(i + 1, end)
        result += left * right
    cache[key] = result
    return result


@pytest.mark.parametrize(
    "n, expected",
    [(2, 2), (3, 5)],
)
def test_count_unique_trees(n, expected):
    assert count_unique_trees(n) == expected
