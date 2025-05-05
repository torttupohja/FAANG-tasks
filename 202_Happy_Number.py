def isHappy(n):
    # Helper function to compute the sum of the squares of digits
    def get_next(number):
        total_sum = 0
        while number > 0:
            digit = number % 10
            total_sum += digit ** 2
            number //= 10
        return total_sum

    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1

"""
Time: Depends on how quickly we detect a cycle, but typically O(log n)
Space: O(log n) → set of seen numbers
"""
