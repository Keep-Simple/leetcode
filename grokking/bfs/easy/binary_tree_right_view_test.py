from collections import deque

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_right_view(root):
    """
    Given a binary tree,
    return an array containing nodes in its right view.
    The right view of a binary tree is the set of nodes visible
    when the tree is seen from the right side.
    """
    queue = deque([root])
    ans = []
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        ans.append(curr.val)
    return ans


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(
                    2,
                    left=TreeNode(4),
                    right=TreeNode(5),
                ),
                right=TreeNode(
                    3,
                    left=TreeNode(6),
                    right=TreeNode(7),
                ),
            ),
            [1, 3, 7],
        ),
        (
            TreeNode(
                12,
                left=TreeNode(
                    7,
                    left=TreeNode(9, left=TreeNode(3)),
                ),
                right=TreeNode(
                    1,
                    left=TreeNode(10),
                    right=TreeNode(5),
                ),
            ),
            [12, 1, 5, 3],
        ),
    ],
)
def test_tree_right_view(root, expected):
    assert tree_right_view(root) == expected
