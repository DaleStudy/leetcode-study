"""
57. Insert Interval
https://leetcode.com/problems/insert-interval/

Solution:
    To solve this problem, we can follow the following steps:
    1. Create an empty list called result to store the final intervals.
    2. Initialize a variable i to 0 to iterate through the intervals.
    3. Iterate through the intervals and add all intervals ending before the new interval starts to the result list.

Time Complexity: O(n)
    -

"""


from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals ending before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge all overlapping intervals with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Add all intervals starting after the new interval ends
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
