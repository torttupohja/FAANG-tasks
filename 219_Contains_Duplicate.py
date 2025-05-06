def containsNearbyDuplicate(nums, k):
    # Dictionary to store the most recent index of each number
    num_indices = {}

    for i, num in enumerate(nums):
        # Check if we've seen this number before
        if num in num_indices:
            # Check if the index difference is within k
            if i - num_indices[num] <= k:
                return True  # Found a valid duplicate

        # Update the most recent index for this number
        num_indices[num] = i

    return False  # No valid duplicates found

"""
Time: O(n) → single pass through the array
Space: O(n) → storing the index of each number
"""
