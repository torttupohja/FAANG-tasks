def longestCommonPrefix(strs):
    # Step 1: Return "" immediately if the list is empty
    if not strs:
        return ""

    # Step 2: Loop through characters in the first string
    for i in range(len(strs[0])):
        # Compare the current character with the same index in all other strings
        for string in strs[1:]:
            # If index is out of range or characters don't match, return prefix up to this point
            if i >= len(string) or string[i] != strs[0][i]:
                return strs[0][:i]

    # If loop completes, the entire first string is a common prefix
    return strs[0]

"""
Time: O(n * m) where n = number of strings, m = length of the shortest string
Space: O(1) – No extra space beyond variables
"""
