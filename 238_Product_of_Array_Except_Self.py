def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n  # Step 1: Initialize result array with 1s

    # Step 2: Build prefix products
    # answer[i] will contain product of all elements to the *left* of i
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]  # Update prefix for next index

    # Step 3: Build suffix products and multiply with existing prefix in answer
    suffix = 1
    for i in reversed(range(n)):
        answer[i] *= suffix  # Multiply prefix and suffix
        suffix *= nums[i]  # Update suffix for previous index

    return answer

"""
Time: O(n) – two passes through the array
Space: O(1) extra (the output array is not counted)
"""
