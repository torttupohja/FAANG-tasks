class TrieNode:
    def __init__(self):
        self.children = {}  # maps char -> TrieNode
        self.is_end = False  # True if node marks end of a word

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """Insert a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """Search with support for '.' wildcard."""
        def dfs(index, node):
            if index == len(word):
                return node.is_end

            char = word[index]

            if char == '.':
                # Try all children at this level
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])

        return dfs(0, self.root)
