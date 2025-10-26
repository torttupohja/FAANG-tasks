def max_subarray(nums):
    best = curr = nums[0]
    for x in nums[1:]:
        curr = max(x, curr + x)
        best = max(best, curr)
    return best

"""
Time complexity: O(n)
Space complexity: O(1)
"""
