def isValid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map:
            # Pop from stack if not empty, else use a dummy value
            top = stack.pop() if stack else '#'
            if bracket_map[char] != top:
                return False
        else:
            stack.append(char)

    return not stack  # stack should be empty if all brackets matched

"""
Time complexity is O(n) — we go through the string once.
Space complexity is O(n) — in the worst case, all characters are opening brackets pushed to the stack.
"""
