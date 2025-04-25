def minSubArrayLen(target, nums):
    n = len(nums)
    left = 0          # Left boundary of the window
    total = 0         # Sum of the current window
    min_length = float('inf')  # Start with an infinitely large minimum length

    # Expand the window with the right pointer
    for right in range(n):
        total += nums[right]

        # Once the window sum is >= target, try shrinking from the left
        while total >= target:
            # Update minimum length
            min_length = min(min_length, right - left + 1)
            # Shrink window from the left
            total -= nums[left]
            left += 1

    # If we never found a valid window, return 0
    return min_length if min_length != float('inf') else 0

"""
Time: O(n) — each element is visited at most twice (once by right, once by left)
Space: O(1) — only variables used, no extra space
"""
