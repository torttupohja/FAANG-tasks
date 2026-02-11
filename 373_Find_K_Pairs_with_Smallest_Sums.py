import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2 or k <= 0:
        return []
    m, n = len(nums1), len(nums2)
    h = []
    for i in range(min(m, k)):
        heapq.heappush(h, (nums1[i] + nums2[0], i, 0))
    res = []
    while h and len(res) < k:
        _, i, j = heapq.heappop(h)
        res.append([nums1[i], nums2[j]])
        if j + 1 < n:
            heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
    return res

"""
Time complexity: O(min(m, k) + k log(min(m, k)))
Space complexity: O(min(m, k))
"""
