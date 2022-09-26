import pytest

from blind_75.trees.utils import array_to_bt


def is_subtree(root, sub_root):
    """
    Given the roots of two binary trees root and subRoot,
    return true if there is a subtree of root with the same structure
    and node values of subRoot and false otherwise.

    A subtree of a binary tree tree is a tree that consists of a node
    in tree and all of this node's descendants.
    The tree tree could also be considered as a subtree of itself.
    """
    if not sub_root:
        return True
    if not root:
        return False
    if same_tree(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


def same_tree(s, t):
    if not s and not t:
        return True
    if s and t and s.val == t.val:
        return same_tree(s.left, t.left) and same_tree(s.right, t.right)
    return False


@pytest.mark.parametrize(
    "root, sub_root, expected",
    [
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
    ],
)
def test_is_subtree(root, sub_root, expected):
    assert is_subtree(array_to_bt(root), array_to_bt(sub_root)) == expected
