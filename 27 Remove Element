def removeElement(nums, val):
    k = 0  # Pointer to store position of non-val elements

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # Move non-val element to the front
            k += 1  # Increase count of non-val elements

    return k  # Number of elements not equal to val

""" 
Explanation
We use a pointer k to track the position of elements not equal to val.
We iterate through the array:
If nums[i] != val, we place it at nums[k] and increment k.
After the loop, k represents the number of valid elements in nums, and the first k positions contain the required elements.
Time & Space Complexity
Time Complexity:
O(n) – We iterate through nums once.
Space Complexity: 
O(1) – We modify nums in-place without extra space.
"""
