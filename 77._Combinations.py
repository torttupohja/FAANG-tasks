def combine(n, k):
    result = []

    def backtrack(start, path):
        # Base case: combination of length k
        if len(path) == k:
            result.append(path[:])
            return

        # Try all remaining numbers from 'start' to 'n'
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)  # Move to the next number
            path.pop()  # Backtrack

    backtrack(1, [])
    return result

"""
Time Complexity: O(C(n, k))
Where C(n, k) is the number of combinations (n choose k)

Space Complexity:
O(k) recursion depth
Output space: O(C(n, k) * k) to store all combinations
"""
