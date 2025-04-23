def plusOne(digits):
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits  # no carry, done
        digits[i] = 0  # set to 0 and continue loop for carry

    # If all digits were 9 → we now need an extra 1 at the beginning
    return [1] + digits

"""
Time complexity is O(n) because we might need to touch every digit.
Space complexity is O(1) extra (modifying in place, result size grows only by 1 max).
"""
