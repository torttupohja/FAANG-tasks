def permute(nums):
    result = []

    def backtrack(path, used):
        # Base case: all elements are used
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue  # Skip already used elements

            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()        # Undo the move
            used[i] = False   # Mark as unused again

    backtrack([], [False] * len(nums))
    return result

"""
Time Complexity: O(n!)
There are n! permutations of a list of n distinct elements.

Space Complexity:
O(n) for the recursion stack
O(n!) for storing the result
"""
