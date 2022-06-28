from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        def r(node: Optional[TreeNode], res: List):
            if node:
                r(node.left, res)
                res.append(node.val)
                r(node.right, res)

        res = []
        r(root, res)

        return res

    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        current_node = root
        res = []

        while stack or current_node:
            if not current_node:
                prev = stack.pop()
                res.append(prev.val)
                current_node = prev.right
            else:
                stack.append(current_node)
                current_node = current_node.left

        return res
