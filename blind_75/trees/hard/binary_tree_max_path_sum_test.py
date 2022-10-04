import math

import pytest

from blind_75.trees.utils import array_to_bt


def max_path_sum(root):
    """
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
    A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
    The path sum of a path is the sum of the node's values in the path.
    Given the root of a binary tree, return the maximum path sum of any non-empty path.

    Solution:
        postorder dfs through the tree,
        for each node return the classic path with max sum
        if sum is negative, return 0 instead (not including it)
        still if all elements are not negative, we can't include every element
        because that won't be a valid sum-path (example below),
        valid sum-path could only have a SINGLE SPLIT at the root node
                 1
              2     3
                  4   5

        update max_sum on each step by taking max-sum path of left and right subtrees
        (max_sum is the SINGLE SPLIT point from above)
    """
    max_sum = -math.inf

    def _max_sum(root):
        nonlocal max_sum
        if not root:
            return 0
        left_s = _max_sum(root.left)
        right_s = _max_sum(root.right)
        # do a single split, update max_sum if needed
        max_sum = max(max_sum, left_s + right_s + root.val)

        # ignore negative sum, fallback to 0 (not including root and its children)
        # return max sum path (without split)
        return max(max(left_s, right_s, 0) + root.val, 0)

    _max_sum(root)
    return max_sum


@pytest.mark.parametrize(
    "root, expected",
    [
        ([1, 2, 3], 6),  # the optimal path 2->1->3 (6)
        ([-10, 9, 20, None, None, 15, 7], 42),  # the optimal path 15->20->7 (42)
        ([2, -1], 2),
    ],
)
def test_max_path_sum(root, expected):
    assert max_path_sum(array_to_bt(root)) == expected
