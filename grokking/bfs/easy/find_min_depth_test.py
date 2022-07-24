from collections import deque

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_minimum_depth(root):
    """
    Find the minimum depth of a binary tree.
    The minimum depth is the number of nodes along the shortest path
    from the root node to the nearest leaf node.
    """
    if not root:
        return 0

    queue = deque([root])
    lvl = 1
    while len(queue) > 0:
        for _ in range(len(queue)):
            curr = queue.popleft()
            if not curr.right and not curr.left:
                return lvl
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        lvl += 1


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                right=TreeNode(3),
            ),
            2,
        ),
        (
            TreeNode(
                12,
                left=TreeNode(7, left=TreeNode(9)),
                right=TreeNode(
                    1, left=TreeNode(10, left=TreeNode(11)), right=TreeNode(5)
                ),
            ),
            3,
        ),
    ],
)
def test_traverse(root, expected):
    assert find_minimum_depth(root) == expected
