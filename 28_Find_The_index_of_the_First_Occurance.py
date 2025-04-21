def strStr(haystack, needle):
    if not needle:
        return 0

    for i in range(0, len(haystack) - len(needle) + 1):  # note: +1 to include last valid position
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1  # only return -1 if loop ends and nothing was found

"""
Time complexity: O(n * m)
Space complexity: O(1)
"""
