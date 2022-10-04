import pytest

"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
    word may contain dots '.' where dots can be matched with any letter.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if not curr.children.get(char):
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(idx, root):
            curr = root

            for i in range(idx, n):
                char = word[i]
                if char == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if not curr.children.get(char):
                        return False
                    curr = curr.children[char]
            return curr.is_end

        return dfs(0, self.trie)


@pytest.mark.parametrize(
    "operations, data, expected",
    [
        (
            [
                "WordDictionary",
                "addWord",
                "addWord",
                "addWord",
                "search",
                "search",
                "search",
                "search",
            ],
            [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
            [None, None, None, None, False, True, True, True],
        )
    ],
)
def test(operations, data, expected):
    trie = None
    for op, d, e in zip(operations, data, expected):
        if op == "WordDictionary":
            trie = WordDictionary()
        elif trie is not None:
            assert getattr(trie, op)(d[0]) == e
