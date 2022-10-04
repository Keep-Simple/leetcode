import pytest

from blind_75.trees.utils import TreeNode, bt_to_array


def build_tree(preorder, inorder):
    """
    Given two integer arrays preorder and inorder where preorder
    is the preorder traversal of a binary tree and inorder is the
    inorder traversal of the same tree, construct and return the binary tree.

    Constraints:
        1 <= preorder.length <= 3000
        inorder.length == preorder.length
        -3000 <= preorder[i], inorder[i] <= 3000
        preorder and inorder consist of unique values.
        Each value of inorder also appears in preorder.
        preorder is guaranteed to be the preorder traversal of the tree.
        inorder is guaranteed to be the inorder traversal of the tree.

    Solution:
        - Preorder -> NLR (Root -> Left -> Right), the root is preorder[0]
        - Inorder -> LNR (Left -> Root -> Right), if we find the root,
            we can recursivly split array into two subtrees

        To find the left and right subtrees, it will look for the root in inorder,
        so that everything on the left should be the left subtree, and everything on the right should be the right subtree.
        Both subtrees can be constructed by making another recursion call.

        Instead of linear searching for root in inorder - we create hashmap
        That reduced TC from O(n^2) to O(n)

        Basically doing preorder (NLR) like traversal (root on line :44, left :48, right :49)
        On each step we take next element from preorder array and split into two brances
        using idx search on inorder array
    """
    n = len(preorder)
    preorder_idx = 0
    inorder_idx_map = {inorder[i]: i for i in range(n)}

    def _build_tree(left, right):
        nonlocal preorder_idx
        if left > right:
            return None

        root = TreeNode(preorder[preorder_idx])
        preorder_idx += 1
        split_idx = inorder_idx_map[root.val]

        root.left = _build_tree(left, split_idx - 1)
        root.right = _build_tree(split_idx + 1, right)

        return root

    return _build_tree(0, n - 1)


@pytest.mark.parametrize(
    "preorder, inorder, expected",
    [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        ([-1], [-1], [-1]),
        ([1, 2], [2, 1], [1, 2, None]),
        ([1, 2], [1, 2], [1, None, 2]),
    ],
)
def test_build_tree(preorder, inorder, expected):
    assert bt_to_array(build_tree(preorder, inorder)) == expected
