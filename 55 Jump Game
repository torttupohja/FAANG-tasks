def canJump(nums):
    # This will store the farthest index we can reach so far
    farthest = 0

    # Iterate through the array
    for i in range(len(nums)):
        # If we're at an index beyond what we can reach, we can't move forward
        if i > farthest:
            return False
        
        # Update the farthest we can reach from this position
        farthest = max(farthest, i + nums[i])

        # Optional early exit: if we've already reached or passed the last index
        if farthest >= len(nums) - 1:
            return True

    # After the loop, check if we can reach the last index
    return farthest >= len(nums) - 1

"""
Time: O(n) – One pass through the array
Space: O(1) – No extra space used
"""
