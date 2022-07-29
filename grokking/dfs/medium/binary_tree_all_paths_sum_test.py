import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    """
    Given a binary tree and a number ‘S’,
    find all paths from root-to-leaf such that the sum
    of all the node values of each path equals ‘S’.
    """
    if not root:
        return None
    queue = [(root, [root.val], root.val)]
    ans = []

    while queue:
        curr, path, path_sum = queue.pop()

        if path_sum == sum and not curr.left and not curr.right:
            ans.append(path)

        if curr.left:
            queue.append(
                (curr.left, path + [curr.left.val], path_sum + curr.left.val),
            )
        if curr.right:
            queue.append(
                (curr.right, path + [curr.right.val], path_sum + curr.right.val),
            )

    return ans


def find_paths_2(root, required_sum):
    allPaths = []
    find_paths_recursive(root, required_sum, [], allPaths)
    return allPaths


def find_paths_recursive(currentNode, required_sum, currentPath, allPaths):
    if currentNode is None:
        return

    # add the current node to the path
    currentPath.append(currentNode.val)

    # if the current node is a leaf and its value is equal to required_sum, save the current path
    if (
        currentNode.val == required_sum
        and currentNode.left is None
        and currentNode.right is None
    ):
        allPaths.append(list(currentPath))
    else:
        # traverse the left sub-tree
        find_paths_recursive(
            currentNode.left, required_sum - currentNode.val, currentPath, allPaths
        )
        # traverse the right sub-tree
        find_paths_recursive(
            currentNode.right, required_sum - currentNode.val, currentPath, allPaths
        )

    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    del currentPath[-1]


@pytest.mark.parametrize(
    "root, sum, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(
                    7,
                    left=TreeNode(4),
                    right=TreeNode(5),
                ),
                right=TreeNode(
                    9,
                    left=TreeNode(2),
                    right=TreeNode(7),
                ),
            ),
            12,
            [[1, 9, 2], [1, 7, 4]],
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
            23,
            [[12, 1, 10], [12, 7, 4]],
        ),
    ],
)
def test_find_paths(root, sum, expected):
    assert find_paths(root, sum) == expected
