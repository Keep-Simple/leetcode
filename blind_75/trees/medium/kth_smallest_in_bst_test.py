import pytest

from blind_75.trees.utils import array_to_bst


def kth_smallest(root, k):
    """
    Given the root of a binary search tree, and an integer k,
    return the kth smallest value (1-indexed) of all the values
    of the nodes in the tree.

    Follow up: If the BST is modified often
    (i.e., we can do insert and delete operations)
    and you need to find the kth smallest frequently,
    how would you optimize?

    Solution:
        Do in-order(LNR) traversal - DFS
        Return k-th element (because LNR traversal of bst is sorted array)
    """
    idx = 0
    ans = None

    def dfs_in_order(root):
        if root is None:
            return
        dfs_in_order(root.left)
        nonlocal idx, ans, k
        idx += 1
        if idx == k:
            ans = root.val
            return
        dfs_in_order(root.right)

    dfs_in_order(root)

    return ans


def kth_smallest_iterative(root, k):
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right


@pytest.mark.parametrize(
    "root, k,expected",
    [
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
    ],
)
def test_kth_smallest(root, k, expected):
    assert kth_smallest(array_to_bst(root), k) == expected
    assert kth_smallest_iterative(array_to_bst(root), k) == expected
