import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    """
    Given a binary tree and a number ‘S’,
    find if the tree has a path from root-to-leaf such
    that the sum of all the node values of that path equals ‘S’.
    """
    queue = [root]
    s = 0

    while queue:
        curr = queue.pop()
        s += curr.val
        if not curr.left and not curr.right:
            if sum == s:
                return True
            else:
                s -= curr.val
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return False


def has_path_recursive(root, sum):
    if root is None:
        return False

    # if the current node is a leaf and its value is equal to the sum, we've found a path
    if root.val == sum and root.left is None and root.right is None:
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


@pytest.mark.parametrize(
    "root, sum, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(
                    2,
                    left=TreeNode(4),
                    right=TreeNode(5),
                ),
                right=TreeNode(
                    3,
                    left=TreeNode(6),
                    right=TreeNode(7),
                ),
            ),
            10,
            True,
        ),
        (
            TreeNode(
                12,
                left=TreeNode(
                    7,
                    left=TreeNode(9),
                ),
                right=TreeNode(
                    1,
                    left=TreeNode(10),
                    right=TreeNode(5),
                ),
            ),
            16,
            False,
        ),
    ],
)
def test_has_path(root, sum, expected):
    assert has_path(root, sum) == expected
    assert has_path_recursive(root, sum) == expected
