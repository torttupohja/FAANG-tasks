def max_subarray_circular(nums):
    total = 0
    max_end = max_so_far = nums[0]
    min_end = min_so_far = nums[0]
    for x in nums:
        total += x
        max_end = max(x, max_end + x)
        max_so_far = max(max_so_far, max_end)
        min_end = min(x, min_end + x)
        min_so_far = min(min_so_far, min_end)
    if max_so_far < 0:
        return max_so_far
    return max(max_so_far, total - min_so_far)

"""
Time complexity: O(n)
Space complexity: O(1)
"""
