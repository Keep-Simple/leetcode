import pytest

from blind_75.trees.utils import array_to_bst, bst_to_array


def invert_tree(root):
    """
    Given the root of a binary tree,
    invert the tree, and return its root.

    Solution:
        DFS iterative traversal, swapping left and right on each step
    """
    if not root:
        return None

    stack = [root]
    while stack:
        node = stack.pop()
        # swap left and right
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root


def invert_tree_recursive(root):
    """
    Same DFS, but recursive
    """
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree_recursive(root.left)
    invert_tree_recursive(root.right)
    return root


@pytest.mark.parametrize(
    "root, expected",
    [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
    ],
)
def test_invert_tree(root, expected):
    assert bst_to_array(invert_tree(array_to_bst(root))) == expected
