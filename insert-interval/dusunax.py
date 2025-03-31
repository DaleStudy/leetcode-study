'''
# 57. Insert Interval

## A. insert first, merge later
- use binary search to find the index of the new interval.(bisect_left)
- insert the new interval into the list.
- iterate through the list and merge the intervals.

## B. insert, merge, insert
- inserting the intervals into the result list until finding the correct index of the new interval.
- merge the overlapping intervals than insert the newInterval into the result list.
- insert the remaining intervals into the result list.
'''
class Solution:
    '''
    # A. insert first, merge later
    - TC: O(n)
    - SC: O(n)
    '''
    def insertUsingBisectLeftToFindIndex(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start_idx = bisect_left([interval[0] for interval in intervals], newInterval[0]) # TC: O(log n)
        
        intervals.insert(start_idx, newInterval) # TC: O(n)

        result = []  # SC: O(n)
        for interval in intervals: # TC: O(n)
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
            
        return result
    
    '''
    # B. insert, merge, insert
    - TC: O(n)
    - SC: O(n)
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = [] # SC: O(n)
        i = 0
        n = len(intervals)

        # 1. insert until finding the correct index of newInterval
        while i < n and intervals[i][1] < newInterval[0]: # TC: O(n)
            result.append(intervals[i])
            i += 1

        # merge overapping intervals & insert newInterval
        while i < n and intervals[i][0] <= newInterval[1]: # TC: O(n)
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        
        while i < n: # TC: O(n)
            result.append(intervals[i])
            i += 1
        
        return result
