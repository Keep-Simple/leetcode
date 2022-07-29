import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_diameter(root):
    """
    Given a binary tree, find the length of its diameter.
    The diameter of a tree is the number of nodes
    on the longest path between any two leaf nodes.
    The diameter of a tree may or may not pass through the root.

    Note: You can always assume that there are
    at least two leaf nodes in the given tree.
    """
    max_diameter = 0

    def find_height_recursive(curr):
        if not curr:
            return 0
        nonlocal max_diameter
        left_h = find_height_recursive(curr.left)
        right_h = find_height_recursive(curr.right)

        # diameter at the current node will be equal to the height of left subtree +
        # the height of right sub-trees + '1' for the current node
        max_diameter = max(max_diameter, right_h + left_h + 1)

        # height of the current node will be equal to the maximum of the heights of
        # left or right subtrees plus '1' for the current node
        return max(left_h, right_h) + 1

    find_height_recursive(root)

    return max_diameter


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
            5,
        ),
        (
            TreeNode(
                1,
                left=TreeNode(
                    2,
                ),
                right=TreeNode(
                    3,
                    left=TreeNode(
                        5,
                        left=TreeNode(7),
                        right=TreeNode(
                            8,
                            left=TreeNode(10),
                        ),
                    ),
                    right=TreeNode(
                        6,
                        left=TreeNode(
                            9,
                            left=TreeNode(11),
                        ),
                    ),
                ),
            ),
            7,
        ),
    ],
)
def test_find_diameter(root, expected):
    assert find_diameter(root) == expected
