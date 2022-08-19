class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True

    def dfs(self, node, pre, output):
        if node.is_end:
            output.append((pre + node.char))

        for child in node.children.values():
            self.dfs(child, pre + node.char, output)

    def search(self, x):
        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        output = []

        self.dfs(node, x[:-1], output)

        return output


tr = Trie()
tr.insert("here")
tr.insert("hear")
tr.insert("he")
tr.insert("hello")
tr.insert("how ")
tr.insert("her")

print(tr.search("he"))
