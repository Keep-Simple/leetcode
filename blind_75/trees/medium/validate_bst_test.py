import math

import pytest

from blind_75.trees.utils import array_to_bt


def is_valid_bst(root):
    """
    Given the root of a binary tree,
    determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:
    1 The left subtree of a node contains only nodes with keys less than the node's key.
    2 The right subtree of a node contains only nodes with keys greater than the node's key.
    3 Both the left and right subtrees must also be binary search trees.

    Solution:
        Validating only 2 children of the current node isn't enough:
            [5]
        1       7
              [3]   9
        (Example) -> 3 < 5, violates 2nd rule

        So we need to keep boundaries of possible values
        Starting from left=-math.inf, right=math.inf,
        we narrow down it as we go down in dfs
            if right child -> update left boundary to node.val
            if left child -> update right boundary to node.val
            As soon as node.val is out of range of boundaries -> return False

        Take a look at iterative and recurisive dfs solutions down below
    """
    if not root:
        return True
    stack = [(root, -math.inf, math.inf)]

    while stack:
        node, min_el, max_el = stack.pop()

        if not (min_el < node.val < max_el):
            return False

        if node.right is not None:
            stack.append((node.right, node.val, max_el))

        if node.left is not None:
            stack.append((node.left, min_el, node.val))

    return True


def is_valid_bst_recursive(root):
    def valid(node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False

        return valid(node.left, left, node.val) and valid(node.right, node.val, right)

    return valid(root, -math.inf, math.inf)


@pytest.mark.parametrize(
    "root, expected",
    [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([2, 2, 2], False),
        ([5, 4, 6, None, None, 3, 7], False),
    ],
)
def test_is_valid_bst(root, expected):
    assert is_valid_bst(array_to_bt(root)) == expected
    assert is_valid_bst_recursive(array_to_bt(root)) == expected
