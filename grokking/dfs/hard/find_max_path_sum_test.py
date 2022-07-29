import math

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_maximum_path_sum(root):
    """
    Find the path with the maximum sum in a given binary tree.
    Write a function that returns the maximum sum.

    A path can be defined as a sequence of nodes between any two nodes
    and doesn’t necessarily pass through the root.
    The path must contain at least one node.
    """
    max_sum = -math.inf

    def find_sum_recursive(curr):
        if not curr:
            return 0
        nonlocal max_sum
        left_s = find_sum_recursive(curr.left)
        right_s = find_sum_recursive(curr.right)
        max_sum = max(max_sum, left_s + right_s + curr.val)
        # ignore negative sum, fallback to 0
        return max(max(left_s, right_s) + curr.val, 0)

    find_sum_recursive(root)
    return max_sum


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(4)),
                right=TreeNode(
                    3,
                    left=TreeNode(5),
                    right=TreeNode(6),
                ),
            ),
            16,
        ),
        (
            TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
                right=TreeNode(
                    3,
                    left=TreeNode(
                        5,
                        left=TreeNode(7),
                        right=TreeNode(8),
                    ),
                    right=TreeNode(
                        6,
                        left=TreeNode(9),
                    ),
                ),
            ),
            31,
        ),
        (
            TreeNode(
                -1,
                left=TreeNode(-3),
            ),
            -1,
        ),
    ],
)
def test_find_maximum_path_sum(root, expected):
    assert find_maximum_path_sum(root) == expected
