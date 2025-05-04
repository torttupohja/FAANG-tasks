def twoSum(nums, target):
    # Dictionary to store number → index
    num_to_index = {}

    # Loop through the list
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # If the complement is already in the map, we found the pair
        if complement in num_to_index:
            return [num_to_index[complement], i]

        # Otherwise, store this number and its index
        num_to_index[num] = i

    # We assume exactly one solution exists, so we don't need a fallback return

"""
Time: O(n) → single pass over the array
Space: O(n) → to store the hashmap
"""
