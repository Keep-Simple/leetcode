from collections import deque

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_zigzag(root):
    """
    Given a binary tree,
    connect each node with its level order successor.
    The last node of each level should point to a null node.
    """
    ans = []
    if not root:
        return ans

    queue = deque([root])
    left_to_right = True
    while len(queue) != 0:
        lvl_size = len(queue)
        lvl_nodes = deque()
        for _ in range(lvl_size):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            if left_to_right:
                lvl_nodes.append(curr.val)
            else:
                lvl_nodes.appendleft(curr.val)
        left_to_right = not left_to_right
        ans.append(list(lvl_nodes))
    return list(ans)


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)),
            ),
            [[1], [3, 2], [4, 5, 6, 7]],
        ),
    ],
)
def test_traverse_zigzag(root, expected):
    assert traverse_zigzag(root) == expected
