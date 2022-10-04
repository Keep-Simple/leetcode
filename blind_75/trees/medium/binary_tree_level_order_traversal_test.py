from collections import deque

import pytest

from blind_75.trees.utils import array_to_bt


def level_order_traversal(root):
    """
    Given the root of a binary tree,
    return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).

    Solution:
        Level by level bfs traversal
    """
    if not root:
        return []

    traversal = []
    queue = deque([root])
    while queue:
        lvl_size = len(queue)
        lvl_traversal = []
        while lvl_size > 0:
            node = queue.popleft()
            lvl_traversal.append(node.val)
            lvl_size -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        traversal.append(lvl_traversal)

    return traversal


@pytest.mark.parametrize(
    "root, expected",
    [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
    ],
)
def test_level_order_traversal(root, expected):
    assert level_order_traversal(array_to_bt(root)) == expected
