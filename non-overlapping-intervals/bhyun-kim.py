"""
435. Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/

Solution:
    To solve this problem, we can follow the following steps:
    1. Sort the intervals based on their end times.
    2. Initialize the end time of the last added interval.
    3. Iterate through the intervals and add non-overlapping intervals to the count.
    4. The number of intervals to remove is the total number minus the count of non-overlapping intervals.

Time Complexity: O(nlogn)
    - Sorting the intervals takes O(nlogn) time.
    - Iterating through the intervals takes O(n) time.
    - Overall, the time complexity is O(nlogn).

Space Complexity: O(1)
    - We are using a constant amount of space to store the end time of the last added interval.
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals based on end times
        intervals.sort(key=lambda x: x[1])

        # Initialize the end time of the last added interval
        end = intervals[0][1]
        count = 1

        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                count += 1
                end = intervals[i][1]

        # The number of intervals to remove is the total number minus the count of non-overlapping intervals
        return len(intervals) - count
