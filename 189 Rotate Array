#Solution 1:
def rotate(nums, k):
  n = len(nums)
  k = k % n  # Normalize k to avoid unnecessary full rotations

  # Create a new rotated version using slicing
  rotated = nums[-k:] + nums[:-k]

  # Copy the rotated result back into the original array
  for i in range(n):
      nums[i] = rotated[i]
"""
Time: O(n)
Space: O(n) (not in-place)
"""

#Solution 2:
def rotate(nums, k):
  n = len(nums)
  k = k % n  # Normalize k

  for _ in range(k):
      # Pop the last element and insert it at the beginning
      last = nums.pop()
      nums.insert(0, last)
"""
Time: O(n * k)
Space: O(1) (in-place)
"""

#Solution 3:
def rotate(nums, k):
  n = len(nums)
  k = k % n  # Normalize k

  # Helper function to reverse a portion of the list
  def reverse(start, end):
      while start < end:
          nums[start], nums[end] = nums[end], nums[start]
          start += 1
          end -= 1

  # Step 1: Reverse the whole array
  reverse(0, n - 1)

  # Step 2: Reverse the first k elements
  reverse(0, k - 1)

  # Step 3: Reverse the rest
  reverse(k, n - 1)
"""
Time: O(n)
Space: O(1)
"""
