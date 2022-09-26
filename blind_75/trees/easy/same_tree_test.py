import pytest

from blind_75.trees.utils import array_to_bt


def is_same_tree(p, q):
    """
    Given the roots of two binary trees p and q,
    write a function to check if they are the same or not.

    Two binary trees are considered the same
    if they are structurally identical, and the nodes have the same value.
    """
    stack = [(p, q)]
    while stack:
        p_node, q_node = stack.pop()
        # xor -> return False if p_node & q_node hold different is None answers
        if (p_node is None) ^ (q_node is None):
            return False
        # p_node and q_node both hold values
        elif p_node is not None:
            if p_node.val != q_node.val:
                return False
            stack.append((p_node.left, q_node.left))
            stack.append((p_node.right, q_node.right))

    return True


@pytest.mark.parametrize(
    "p, q, expected",
    [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
    ],
)
def test_is_same_tree(p, q, expected):
    assert is_same_tree(array_to_bt(p), array_to_bt(q)) == expected
