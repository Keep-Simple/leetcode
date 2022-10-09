import pytest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.refs = 0
        self.end_info = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word, end_info=True):
        curr = self.root

        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
            curr.refs += 1

        curr.end_info = end_info

    def remove_word(self, word):
        curr = self.root
        for char in word:
            if char in curr.children:
                temp = curr.children[char]
                temp.refs -= 1
                if temp.refs == 0:
                    del curr.children[char]
                    break
                else:
                    curr = temp
            else:
                break


def find_words(board, words):
    """
    Given an m x n board of characters and a list of strings words,
    return all words on the board.

    Each word must be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once in a word.

    Constraints:
        m == board.length
        n == board[i].length
        1 <= m, n <= 12
        board[i][j] is a lowercase English letter.
        1 <= words.length <= 3 * 104
        1 <= words[i].length <= 10
        words[i] consists of lowercase English letters.
        All the strings of words are unique.

    Solution:
        Backtracking (dfs) with trie
        Check code comments for more
    """
    trie = Trie()
    for i, word in enumerate(words):
        # save word idx at the end node to save memory
        trie.add_word(word, i)

    # up, right, down, left
    m = len(board)  # rows
    n = len(board[0])  # columns
    visited = [[False for _ in range(n)] for _ in range(m)]
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    found_words = []

    def walk_board(y, x, prev_trie_node):
        if not (0 <= x < n and 0 <= y < m) or visited[y][x]:
            return

        char = board[y][x]
        if char not in prev_trie_node.children:
            return

        # visited can be removed, save "#" to the board instead
        # to indicate visited state, and during backtracking bring
        # the char back
        visited[y][x] = True

        trie_node = prev_trie_node.children[char]

        if trie_node.end_info is not None:
            w = words[trie_node.end_info]
            trie_node.end_info = None  # prevents duplicates
            found_words.append(w)
            # decreases reference count for each letter in the word.
            # If it becomes 0 - removes it and it's children from memory
            trie.remove_word(w)

        for delta_y, delta_x in moves:
            walk_board(y + delta_y, x + delta_x, trie_node)

        visited[y][x] = False

    for y in range(m):
        for x in range(n):
            walk_board(y, x, trie.root)

    return found_words


@pytest.mark.parametrize(
    "board,words, expected",
    [
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            ["eat", "oath"],
        ),
        (
            [
                ["a", "b"],
                ["c", "d"],
            ],
            ["abcb"],
            [],
        ),
        (
            [["a", "a"]],
            ["aaa"],
            [],
        ),
    ],
)
def test_find_words(board, words, expected):
    assert sorted(find_words(board, words)) == sorted(expected)
