from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = float('-inf')
        for start, finish in intervals:
            if start < end:
                count += 1
            else:
                end = finish
        return count
