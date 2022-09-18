import pytest


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def find_distance_unbalanced_bst(values, n, node1, node2):
    if n < 2 or len(values) != n or node1 == node2:
        return 0

    if node1 not in values or node2 not in values:
        return -1

    # construct binary tree
    bst_root = None
    for value in values:
        new_node = TreeNode(value)

        if bst_root is None:
            bst_root = new_node
            continue

        curr_node = bst_root
        while True:
            if curr_node.value < new_node.value:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    curr_node.right = new_node
                    break
            elif curr_node.value < new_node.value:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = new_node
                    break
            # node already in the tree
            else:
                break

    # Finding path between node1 and node2
    # 1. find traversals for node1 and node 2
    # 2. find last equal element in traversal, closest parent for node1 and node2
    # 3. sum distance from parent to node1 and node2
    node1_traversal = _find_traversal(bst_root, node1)
    node2_traversal = _find_traversal(bst_root, node2)

    i = 0
    while True:
        if node1_traversal[i] != node2_traversal[i]:
            break
        i += 1

    return len(node1_traversal) - i + len(node2_traversal) - i


def _find_traversal(bst_root, value):
    curr_node = bst_root
    traversal = []

    while curr_node:
        traversal.append(curr_node.value)
        if curr_node.value > value:
            curr_node = curr_node.left
        elif curr_node.value < value:
            curr_node = curr_node.right
        else:
            return traversal

    return None


@pytest.mark.parametrize(
    "values, n, node1, node2, expected",
    [
        ([5, 6, 3, 1, 2, 4], 6, 2, 4, 3),  # resulting path of len 3: 2->1->3
    ],
)
def test_find_distance_unbalanced_bst(values, n, node1, node2, expected):
    assert find_distance_unbalanced_bst(values, n, node1, node2) == expected
