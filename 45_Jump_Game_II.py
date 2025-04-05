def jump(nums):
    n = len(nums)
    
    # If the array has only one element, we're already at the end
    if n == 1:
        return 0

    # Initialize counters
    jumps = 0           # Total number of jumps made
    current_end = 0     # The farthest index we can reach with the current jump
    farthest = 0        # The farthest index we can reach in the next jump

    # We don't need to consider the last index in the loop
    for i in range(n - 1):
        # Update the farthest we can reach from this position
        farthest = max(farthest, i + nums[i])

        # If we've reached the end of the current jump range
        if i == current_end:
            jumps += 1            # We must make another jump
            current_end = farthest  # Update the jump range

            # Early exit: if we've already reached or passed the last index
            if current_end >= n - 1:
                break

    return jumps

"""
Time: O(n) – Single pass through the array
Space: O(1) – No extra space used
"""
