from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort the intervals based on their end times
        # to include as many meetings as possible
        intervals.sort(key=lambda x: x[1])

        # the count of non-overlapping intervals
        count = 0
        # the end time of the last added interval
        end = float("-inf")

        for interval in intervals:
            if interval[0] >= end:
                # If the current interval does not overlap with the last added interval, include it
                end = interval[1]
            else:
                # Otherwise, increment the count of intervals to be removed
                count += 1

        return count
