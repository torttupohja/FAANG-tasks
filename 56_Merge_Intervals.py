from operator import itemgetter

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort(key=itemgetter(0))
        merged = []
        current_start, current_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= current_end:
                current_end = max(current_end, end)
            else:
                merged.append([current_start, current_end])
                current_start, current_end = start, end

        merged.append([current_start, current_end])
        return merged

"""
Time Complexity:
( O(n log n) ) for sorting.
( O(n) ) for merging.
Overall: ( O(n log n) )
Space Complexity: ( O(n) ) for storing the result.
"""
