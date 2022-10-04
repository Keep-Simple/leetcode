from typing import Optional

import pytest

"""
    A trie (pronounced as "try") or prefix tree is a tree data structure
    used to efficiently store and retrieve keys in a dataset of strings.
    There are various applications of this data structure,
    such as autocomplete and spellchecker.

    Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    boolean starts_with(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if curr.children.get(char) is None:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def _search(self, s: str) -> Optional[TrieNode]:
        curr = self.root
        for char in s:
            if not curr.children.get(char):
                return None
            curr = curr.children[char]
        return curr

    def search(self, word: str) -> bool:
        node = self._search(word)
        return node.is_end if node else False

    def starts_with(self, prefix: str) -> bool:
        return self._search(prefix) is not None


@pytest.mark.parametrize(
    "operations, data, expected",
    [
        (
            ["Trie", "insert", "search", "search", "starts_with", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True],
        )
    ],
)
def test_trie(operations, data, expected):
    trie = None
    for op, d, e in zip(operations, data, expected):
        if op == "Trie":
            trie = Trie()
        elif trie is not None:
            assert getattr(trie, op)(d[0]) == e
