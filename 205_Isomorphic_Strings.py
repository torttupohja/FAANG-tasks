def isIsomorphic(s, t):
    if len(s) != len(t):
        return False  # Different lengths → can't be isomorphic

    # Dictionaries to track mappings between s → t and t → s
    s_to_t = {}
    t_to_s = {}

    for c1, c2 in zip(s, t):
        # Check forward mapping s → t
        if c1 in s_to_t:
            if s_to_t[c1] != c2:
                return False  # Inconsistent mapping
        else:
            s_to_t[c1] = c2

        # Check reverse mapping t → s (to prevent two c1 mapping to same c2)
        if c2 in t_to_s:
            if t_to_s[c2] != c1:
                return False  # Inconsistent reverse mapping
        else:
            t_to_s[c2] = c1

    return True  # Passed all checks

"""
Time: O(n) — iterate once through strings
Space: O(n) — for the two mappings
"""
