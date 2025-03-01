'''
시간 복잡도: O(n log n)
공간 복잡도: O(1)
'''
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        iter_intervals = iter(intervals)
        prev_end = next(iter_intervals)[1]

        for start, end in iter_intervals:
            if prev_end > start:
                count += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        
        return count
