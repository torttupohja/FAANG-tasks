def generateParenthesis(n):
    result = []

    def backtrack(open_used, close_used, path):
        # If we've placed n opens and n closes, record a valid string
        if open_used == n and close_used == n:
            result.append("".join(path))
            return

        # Add '(' if we still can
        if open_used < n:
            path.append('(')
            backtrack(open_used + 1, close_used, path)
            path.pop()

        # Add ')' only if it won't break validity (must have an unmatched '(')
        if close_used < open_used:
            path.append(')')
            backtrack(open_used, close_used + 1, path)
            path.pop()

    backtrack(0, 0, [])
    return result
