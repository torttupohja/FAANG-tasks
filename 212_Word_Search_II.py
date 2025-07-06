class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores full word at end node for quick result collection

def build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # Store word at the end node
    return root

def findWords(board, words):
    rows, cols = len(board), len(board[0])
    result = []
    root = build_trie(words)

    def dfs(r, c, node):
        char = board[r][c]
        if char not in node.children:
            return

        next_node = node.children[char]
        if next_node.word:
            result.append(next_node.word)
            next_node.word = None  # Avoid duplicates

        # Mark visited
        board[r][c] = '#'

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                dfs(nr, nc, next_node)

        board[r][c] = char  # Restore original character

        # Optional pruning: remove leaf nodes
        if not next_node.children:
            node.children.pop(char)

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return result

"""
Time Complexity:
Building Trie: O(W * L)
(W = number of words, L = average word length)
DFS Search: O(M * N * 4^L) in the worst case
(M x N = board size, L = max word length)

Space Complexity:
Trie: O(W * L)
Call stack: up to O(L) for DFS
Visited state is maintained in-place by marking with '#'
"""
