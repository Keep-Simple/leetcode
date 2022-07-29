import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    """
    Given a binary tree where each node can only have a digit (0-9) value,
    each root-to-leaf path will represent a number.
    Find the total sum of all the numbers represented by all paths.
    """
    queue = [(root, root.val)]
    ans = 0

    while queue:
        curr, digit_sum = queue.pop()
        if not curr.left and not curr.right:
            ans += digit_sum

        if curr.left:
            queue.append((curr.left, digit_sum * 10 + curr.left.val))
        if curr.right:
            queue.append((curr.right, digit_sum * 10 + curr.right.val))
    return ans


@pytest.mark.parametrize(
    "root, expected",
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
            408,
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
            332,
        ),
    ],
)
def test_find_sum_of_path_numbers(root, expected):
    assert find_sum_of_path_numbers(root) == expected
