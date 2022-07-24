from collections import deque

import pytest


class TreeNode:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def level_order_traversal(self):
        next_level_root = self
        ans = []
        while next_level_root:
            current = next_level_root
            next_level_root = None
            while current:
                ans.append(current.val)
                if not next_level_root:
                    if current.left:
                        next_level_root = current.left
                    elif current.right:
                        next_level_root = current.right
                current = current.next
        return ans


def connect_level_order_siblings(root):
    """
    Given a binary tree,
    connect each node with its level order successor.
    The last node of each level should point to a null node.
    """
    queue = deque([root])
    while queue:
        lvl_size = len(queue)
        for i in range(lvl_size):
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            curr.next = queue[0] if queue and i != lvl_size - 1 else None


@pytest.mark.parametrize(
    "root, expected",
    [
        (
            TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)),
            ),
            [1, 2, 3, 4, 5, 6, 7],
        ),
        (
            TreeNode(
                12,
                left=TreeNode(7, left=TreeNode(9)),
                right=TreeNode(1, left=TreeNode(10), right=TreeNode(5)),
            ),
            [12, 7, 1, 9, 10, 5],
        ),
    ],
)
def test_connect_level_order_siblings(root, expected):
    connect_level_order_siblings(root)
    assert root.level_order_traversal() == expected
