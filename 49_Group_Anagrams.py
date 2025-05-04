from collections import defaultdict

def groupAnagrams(strs):
    # Use defaultdict to automatically create empty lists
    anagrams = defaultdict(list)

    for word in strs:
        # Sort the word to get its anagram signature (e.g., 'eat' → 'aet')
        key = ''.join(sorted(word))

        # Append the original word under its sorted key
        anagrams[key].append(word)

    # Return just the grouped lists
    return list(anagrams.values())

"""
Time: O(n * k log k) →
n = number of words,
k = max word length (because sorting each word takes O(k log k))

Space: O(n * k) → storing all words in groups
"""
