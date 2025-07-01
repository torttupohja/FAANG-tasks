from collections import deque

def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0  # No path possible

    queue = deque([(beginWord, 1)])  # (current_word, steps)
    visited = set([beginWord])
    word_len = len(beginWord)

    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps

        # Try changing each character
        for i in range(word_len):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == word[i]:
                    continue
                next_word = word[:i] + c + word[i+1:]
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, steps + 1))

    return 0  # No transformation sequence found
