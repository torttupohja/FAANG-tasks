class TrieNode:
    def __init__(self):
        self.children = {}  # maps char -> TrieNode
        self.is_end = False  # True if this node marks the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # create new path
            node = node.children[char]
        node.is_end = True  # mark the end of the word

    def search(self, word):
        """Return True if the word exists in the trie."""
        node = self._traverse(word)
        return node is not None and node.is_end

    def startsWith(self, prefix):
        """Return True if there exists any word starting with the prefix."""
        return self._traverse(prefix) is not None

    def _traverse(self, string):
        """Helper to traverse the Trie based on input string."""
        node = self.root
        for char in string:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

"""
Time Complexity: O(L)
Each character is processed once.

Space Complexity:
O(N * L) for insert across all words (N = number of words).
Each node has a dictionary of up to 26 children (for lowercase letters).
"""
