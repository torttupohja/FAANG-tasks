import random

def find_kth_largest(nums, k):
    k = len(nums) - k

    def select(left, right):
        pivot_index = random.randint(left, right)
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        pivot = nums[right]
        store = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1
        nums[store], nums[right] = nums[right], nums[store]

        if store == k:
            return nums[store]
        if store < k:
            return select(store + 1, right)
        return select(left, store - 1)

    return select(0, len(nums) - 1)

"""
Time complexity:
Average: O(n)
Worst case: O(n²)

Space complexity:
O(1) (ignoring recursion stack)"""
