from collections import deque

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_level_avarages(root):
    """
    Given a binary tree,
    populate an array to represent the averages of all of its levels.
    """
    ans = []
    if not root:
        return ans

    queue = deque([root])
    while len(queue) != 0:
        lvl_size = len(queue)
        lvl_nodes_avg = 0
        for _ in range(lvl_size):
            curr = queue.popleft()
            lvl_nodes_avg += curr.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        ans.append(lvl_nodes_avg / lvl_size)
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
            [1, 2.5, 5.5],
        ),
    ],
)
def test_traverse(root, expected):
    assert find_level_avarages(root) == expected
