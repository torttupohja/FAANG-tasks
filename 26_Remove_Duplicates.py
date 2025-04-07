def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1  # Pointer for the position of the next unique element

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

"""
Time Complexity: O(n) – One pass through the array.
Space Complexity: O(1) – In-place modification, no extra space used.
"""
