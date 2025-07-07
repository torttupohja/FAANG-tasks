def letterCombinations(digits):
    if not digits:
        return []

    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    result = []

    def backtrack(index, path):
        # Base case: full combination built
        if index == len(digits):
            result.append("".join(path))
            return

        # Explore all letters for current digit
        for char in phone_map[digits[index]]:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()  # backtrack

    backtrack(0, [])
    return result

"""
Time Complexity: O(4^n)
Worst case when all digits map to 4 letters (e.g., '7' or '9')
n = number of digits

Space Complexity: O(n)
For recursion call stack and temporary path
"""
