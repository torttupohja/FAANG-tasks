from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        res = []

        for i in range(len(nums) - 2):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # need a larger sum
                else:
                    right -= 1  # need a smaller sum

        return res

"""
Time Complexity: O(n^2)

Sorting takes O(n log n)

Outer loop: O(n)

Inner two-pointer loop: O(n) → total O(n²)

Space Complexity: O(1) extra (excluding output list)
"""
