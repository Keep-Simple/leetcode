from collections import deque

import pytest

from blind_75.trees.utils import array_to_bt


def max_depth(root):
    """
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along
    the longest path from the root node down to the farthest leaf node.

    Solution:
        Use level by level BFS
    """
    if not root:
        return 0

    queue = deque([root])
    depth = 0

    while queue:
        lvl_nodes_count = len(queue)
        depth += 1
        for _ in range(lvl_nodes_count):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


@pytest.mark.parametrize(
    "root, expected",
    [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
    ],
)
def test_max_depth(root, expected):
    assert max_depth(array_to_bt(root)) == expected
