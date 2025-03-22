'''
시간 복잡도: O(n)
공간 복잡도: O(n)
'''
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        start, end = newInterval
        i = 0
        result = []

        # before merging
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1
        
        # merge
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])
            
        # after merging
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
