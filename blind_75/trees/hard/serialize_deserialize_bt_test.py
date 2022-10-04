import pytest

from blind_75.trees.utils import TreeNode, array_to_bt, bt_to_array

"""
Serialization is the process of converting a data structure or object
into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification:
    The input/output format is the same as how LeetCode serializes a binary tree.
    You do not necessarily need to follow this format,
    so please be creative and come up with different approaches yourself.


Solution:
    serilalize: do a preorder dfs traversal for None child - save _end_mark instead
    deserialize: do a preorder dfs, keeping idx global
        base case - we see _end_mark at current idx -> return None
        create node for current idx + increment idx, recursivly call for left and right
        return node
"""


class Codec:
    _end_mark = "e"
    _separator = ","

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        arr = []

        def dfs(root):
            if root is None:
                arr.append(self._end_mark)
            else:
                arr.append(str(root.val))
                dfs(root.left)
                dfs(root.right)

        dfs(root)

        return self._separator.join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        arr = data.split(self._separator)
        idx = 0

        def dfs():
            nonlocal idx
            if arr[idx] == self._end_mark:
                idx += 1
                return None
            node = TreeNode(int(arr[idx]))
            idx += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


@pytest.mark.parametrize(
    "root",
    [
        ([1, 2, 3, None, None, 4, 5]),
        ([]),
    ],
)
def test_encode_string(root):
    c = Codec()
    assert bt_to_array(c.deserialize(c.serialize(array_to_bt(root)))) == root
