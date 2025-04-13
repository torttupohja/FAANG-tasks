def trap(height):
    if not height:
        return 0

    # Initialize pointers and variables
    left, right = 0, len(height) - 1           # Two pointers from both ends
    left_max, right_max = 0, 0                 # Track the max height seen from left and right
    trapped_water = 0                          # Total water trapped

    # Process the elevation map
    while left < right:
        if height[left] < height[right]:
            # Work with the left pointer
            if height[left] >= left_max:
                left_max = height[left]        # Update left max
            else:
                # Water trapped is the difference between left_max and current height
                trapped_water += left_max - height[left]
            left += 1
        else:
            # Work with the right pointer
            if height[right] >= right_max:
                right_max = height[right]      # Update right max
            else:
                trapped_water += right_max - height[right]
            right -= 1

    return trapped_water

"""
Time: O(n) – Single pass using two pointers
Space: O(1) – Constant space, no extra arrays used
"""
