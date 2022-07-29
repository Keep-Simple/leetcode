import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    """
    Given a binary tree and a number sequence,
    find if the sequence is present as a root-to-leaf path in the given tree.
    """
    if not root or not sequence:
        return False

    queue = [root]
    cursor = 0

    while queue:
        curr = queue.pop()
        if curr.val == sequence[cursor]:
            cursor += 1
            if cursor == len(sequence):
                return True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    return False


@pytest.mark.parametrize(
    "root, sequence, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(
                    7,
                ),
                right=TreeNode(
                    9,
                    left=TreeNode(2),
                    right=TreeNode(9),
                ),
            ),
            [1, 9, 9],
            True,
        ),
        (
            TreeNode(
                1,
                left=TreeNode(
                    0,
                    left=TreeNode(1),
                ),
                right=TreeNode(
                    1,
                    left=TreeNode(6),
                    right=TreeNode(5),
                ),
            ),
            [1, 0, 7],
            False,
        ),
        (
            TreeNode(
                1,
                left=TreeNode(
                    0,
                    left=TreeNode(1),
                ),
                right=TreeNode(
                    1,
                    left=TreeNode(6),
                    right=TreeNode(5),
                ),
            ),
            [1, 1, 6],
            True,
        ),
    ],
)
def test_find_path(root, sequence, expected):
    assert find_path(root, sequence) == expected
