import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    """
    Given a binary tree and a number ‘S’,
    find all paths in the tree such that the sum
    of all the node values of each path equals ‘S’.
    Please note that the paths can start or end at any node
    but all paths must follow direction from parent to child (top to bottom).
    """
    if not root:
        return 0

    queue = [(root, [], 0, 0)]
    ans = 0

    while queue:
        curr, path, path_sum, window_start = queue.pop()
        path_sum += curr.val
        path = path + [curr.val]
        while path_sum >= S and window_start < len(path):
            if path_sum == S:
                ans += 1
            path_sum -= path[window_start]
            window_start += 1

        if curr.left:
            queue.append((curr.left, path, path_sum, window_start))
        if curr.right:
            queue.append((curr.right, path, path_sum, window_start))

    return ans


def count_paths_recursive(curr, S, path=[], path_sum=0, window_start=0):
    if not curr:
        return 0

    path.append(curr.val)
    path_sum += curr.val
    ans = 0

    while path_sum >= S and window_start < len(path):
        if path_sum == S:
            ans += 1
            break
        path_sum -= path[window_start]
        window_start += 1

    ans += count_paths_recursive(
        curr.left, S, path, path_sum, window_start
    ) + count_paths_recursive(curr.right, S, path, path_sum, window_start)

    # remove the current node from the path to backtrack
    # we need to remove the current node while we are going up the recursive call stack
    path.pop()

    return ans


@pytest.mark.parametrize(
    "root, S, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(7, left=TreeNode(6), right=TreeNode(5)),
                right=TreeNode(
                    9,
                    left=TreeNode(2),
                    right=TreeNode(3),
                ),
            ),
            12,
            3,
        ),
        (
            TreeNode(
                12,
                left=TreeNode(
                    7,
                    left=TreeNode(4),
                ),
                right=TreeNode(
                    1,
                    left=TreeNode(10),
                    right=TreeNode(5),
                ),
            ),
            11,
            2,
        ),
    ],
)
def test_count_paths(root, S, expected):
    assert count_paths(root, S) == expected
    assert count_paths_recursive(root, S) == expected
