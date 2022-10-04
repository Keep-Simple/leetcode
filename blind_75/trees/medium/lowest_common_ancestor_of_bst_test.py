import pytest

from blind_75.trees.utils import array_to_bst


def lowest_common_ancestor(root, p, q):
    """
    Given a binary search tree (BST),
    find the lowest common ancestor (LCA) node of two given nodes in the BST.

    According to the definition of LCA on Wikipedia:
        “The lowest common ancestor is defined between two nodes p and q
        as the lowest node in T that has both p and q as descendants
        (where we allow a node to be a descendant of itself).”

    Constraints:
    - The number of nodes in the tree is in the range [2, 105].
    - -109 <= Node.val <= 109
    - All Node.val are unique.
    - p != q
    - p and q will exist in the BST.

    Solution:
        Find traversals to p and q
        Reverse-Iterate over them in parallel, return the first equal elemnts
    """
    p_traversal = _find_bst_traversal(root, p)
    q_traversal = _find_bst_traversal(root, q)

    if p_traversal and q_traversal:
        for i in range(min(len(p_traversal), len(q_traversal)) - 1, -1, -1):
            if p_traversal[i] == q_traversal[i]:
                return p_traversal[i]
    return None


def _find_bst_traversal(root, node_val):
    if node_val is None:
        return []

    traversal = []
    curr = root

    while curr is not None:
        traversal.append(curr.val)
        if curr.val > node_val:
            curr = curr.left
        elif curr.val < node_val:
            curr = curr.right
        else:
            return traversal

    return []


def lowest_common_ancestor_2(root, p, q):
    """
    Wow, awesome solution
    Do a regular binary tree search, but for 2 nodes at the same time
    As soon as they want to peek different branches -> return
    """
    cur = root
    while cur:
        if p > cur.val and q > cur.val:
            cur = cur.right
        elif p < cur.val and q < cur.val:
            cur = cur.left
        else:
            return cur.val


@pytest.mark.parametrize(
    "root, p, q, expected",
    [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),
        ([2, 1], 2, 1, 2),
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 0, 8, 6),
    ],
)
def test_lowest_common_ancestor(root, p, q, expected):
    assert lowest_common_ancestor(array_to_bst(root), p, q) == expected
    assert lowest_common_ancestor_2(array_to_bst(root), p, q) == expected
