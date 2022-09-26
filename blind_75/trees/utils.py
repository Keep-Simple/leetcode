from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def array_to_bst(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    for i in range(1, len(arr)):
        cursor = root
        el = arr[i]
        if el is None:
            continue

        while True:
            if cursor.val > el:
                if not cursor.left:
                    cursor.left = TreeNode(el)
                    break
                else:
                    cursor = cursor.left
            else:
                if not cursor.right:
                    cursor.right = TreeNode(el)
                    break
                else:
                    cursor = cursor.right

    return root


def array_to_bt(arr):
    """
    BFS traversal (array representation) to binary tree (not binary search tree)
    """
    if not arr:
        return None

    root = TreeNode(arr[0])

    queue = deque([root])
    cursor = 1

    while cursor < len(arr) - 1:
        node = queue.popleft()
        node.left = TreeNode(arr[cursor])
        queue.append(node.left)
        node.right = TreeNode(arr[cursor + 1])
        queue.append(node.right)
        cursor += 2

    return root


def bst_to_array(root):
    """
    Do bfs traversal
    """
    if not root:
        return []

    queue = deque([root])
    arr = []

    while queue:
        node = queue.popleft()
        arr.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return arr
