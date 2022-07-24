from collections import deque

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_successor(root, key):
    """
    Given a binary tree and a node,
    find the level order successor of the given node in the tree.
    The level order successor is the node that appears right after
    the given node in the level order traversal.
    """
    if not root:
        return None

    queue = deque([root])
    while queue:
        curr = queue.popleft()
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        if curr.val == key:
            break

    return queue[0] if queue else None


@pytest.mark.parametrize(
    "root, key, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                right=TreeNode(3),
            ),
            3,
            4,
        ),
        (
            TreeNode(
                12,
                left=TreeNode(7, left=TreeNode(9)),
                right=TreeNode(
                    1, left=TreeNode(10, left=TreeNode(11)), right=TreeNode(5)
                ),
            ),
            9,
            10,
        ),
        (
            TreeNode(
                12,
                left=TreeNode(7, left=TreeNode(9)),
                right=TreeNode(
                    1, left=TreeNode(10, left=TreeNode(11)), right=TreeNode(5)
                ),
            ),
            12,
            7,
        ),
    ],
)
def test(root, key, expected):
    assert find_successor(root, key).val == expected
