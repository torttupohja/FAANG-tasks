def combinationSum(candidates, target):
    candidates.sort()
    result = []
    path = []

    def backtrack(start, remain):
        # If we've hit the target, record the current combination
        if remain == 0:
            result.append(path[:])
            return
        # Try each candidate from 'start' onward
        for i in range(start, len(candidates)):
            val = candidates[i]
            # Prune: no need to continue if current value exceeds remain
            if val > remain:
                break
            path.append(val)
            # Not advancing i allows reuse of the same number (unlimited use)
            backtrack(i, remain - val)
            path.pop()

    backtrack(0, target)
    return result
