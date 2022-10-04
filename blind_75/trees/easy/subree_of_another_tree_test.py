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
    # pick dfs iteratrive, as it's more memory efficient than dfs
    stack = [root]
    while stack:
        node = stack.pop()
        if node and sub_root:
            if _is_same_tree(node, sub_root):
                return True
            stack.append(node.left)
            stack.append(node.right)

    return False


def _is_same_tree(root1, root2):
    stack = [(root1, root2)]
    while stack:
        n1, n2 = stack.pop()
        if (n2 is None) ^ (n1 is None):
            return False
        if n1 is not None:
            if n1.val != n2.val:
                return False
            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))

    return True


def is_subtree_recursive(root, sub_root):
    if not sub_root:
        return True
    if not root:
        return False
    if _same_tree(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


def _same_tree(s, t):
    if not s and not t:
        return True
    if s and t and s.val == t.val:
        return _same_tree(s.left, t.left) and _same_tree(s.right, t.right)
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
    assert is_subtree_recursive(array_to_bt(root), array_to_bt(sub_root)) == expected
