def merge(nums1, m, nums2, n):
    # Pointers for nums1 and nums2 (starting from the end of meaningful elements)
    p1, p2 = m - 1, n - 1
    # Pointer for placing elements in nums1 (starting from the end)
    p = m + n - 1

    # Merge from the back to avoid overwriting elements in nums1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2, copy them over
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
