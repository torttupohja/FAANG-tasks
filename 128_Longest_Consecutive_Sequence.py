def longestConsecutive(nums):
    num_set = set(nums)  # Convert list to set for O(1) lookups
    longest = 0

    for num in num_set:
        # Only start counting if `num` is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count how long the consecutive streak goes
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest

"""
Time: O(n) → each number is visited once
Space: O(n) → for the set
"""
