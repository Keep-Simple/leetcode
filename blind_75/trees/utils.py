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
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    n = len(arr)

    queue = deque([root])

    idx = 0
    while idx < n:
        parent = queue.popleft()
        idx += 1
        if idx < n and arr[idx] is not None:
            parent.left = TreeNode(arr[idx])
            queue.append(parent.left)
        idx += 1
        if idx < n and arr[idx] is not None:
            parent.right = TreeNode(arr[idx])
            queue.append(parent.right)

    return root


def bt_to_array(root):
    """
    Do bfs traversal, (level by level)
    """
    if not root:
        return []

    queue = deque([root])
    arr = []

    while queue:
        lvl_size = len(queue)
        new_queue = []
        has_values = False

        for i in range(lvl_size):
            node = queue[i]
            if node is not None:
                has_values = True
                new_queue.append(node.left)
                new_queue.append(node.right)

        if has_values:
            arr.extend(map(lambda el: el.val if el else None, queue))

        queue = new_queue

    return arr
