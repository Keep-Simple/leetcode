from typing import List

import pytest
from binary_tree_inorder_traversal import Solution, TreeNode


@pytest.mark.parametrize(
    "input,expected",
    [
        (TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3))), [1, 3, 2]),
        (None, []),
        (TreeNode(1), [1]),
    ],
)
def test_solution(input: TreeNode, expected: List) -> None:
    solution = Solution()
    assert solution.inorderTraversalRecursive(input) == expected
    assert solution.inorderTraversalIterative(input) == expected
