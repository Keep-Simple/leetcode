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


def find_unique_trees(n):
    """
    Given a number ‘n’,
    write a function to return all structurally
    unique Binary Search Trees (BST) that can store values 1 to ‘n’?
    """
    if n <= 0:
        return []

    return _find_recursive(1, n)


def _find_recursive(start, end):
    if end < start:
        return [None]

    result = []
    for i in range(start, end + 1):
        left = _find_recursive(start, i - 1)
        right = _find_recursive(i + 1, end)
        for l in left:
            for r in right:
                result.append(TreeNode(val=i, left=l, right=r))
    return result


@pytest.mark.parametrize(
    "n, expected",
    [
        (
            2,
            [
                TreeNode(1, right=TreeNode(2)),
                TreeNode(2, left=TreeNode(1)),
            ],
        ),
        (
            3,
            [
                TreeNode(1, right=TreeNode(2, right=TreeNode(3))),
                TreeNode(1, right=TreeNode(3, left=TreeNode(2))),
                TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
                TreeNode(3, left=TreeNode(1, right=TreeNode(2))),
                TreeNode(3, left=TreeNode(2, left=TreeNode(1))),
            ],
        ),
    ],
)
def test_find_unique_trees(n, expected):
    assert find_unique_trees(n) == expected
