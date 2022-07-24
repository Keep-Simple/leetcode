from collections import deque

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_reverse(root):
    """
    Given a binary tree,
    populate an array to represent its level-by-level traversal
    in reverse order, i.e., the lowest level comes first.
    You should populate the values of all nodes in each level
    from left to right in separate sub-arrays.
    """
    ans = deque([])
    if not root:
        return ans

    queue = deque([root])
    while len(queue) != 0:
        lvl_size = len(queue)
        lvl_nodes = []
        for _ in range(lvl_size):
            curr = queue.popleft()
            lvl_nodes.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        ans.appendleft(lvl_nodes)
    return list(ans)


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                12,
                left=TreeNode(7, left=TreeNode(9)),
                right=TreeNode(1, left=TreeNode(10), right=TreeNode(5)),
            ),
            [[9, 10, 5], [7, 1], [12]],
        ),
    ],
)
def test_traverse_reverse(root, expected):
    assert traverse_reverse(root) == expected
