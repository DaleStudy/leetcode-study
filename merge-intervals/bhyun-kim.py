"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Solution:
    To solve this problem, we can follow the following steps:
    1. Sort the intervals by their start times.
    2. Initialize an empty list called merged to store the final merged intervals.
    3. Iterate through the sorted intervals and merge the current interval with the previous interval if there is an overlap.

Time Complexity: O(nlogn)
    - Sorting the intervals takes O(nlogn) time.
    - Merging the intervals takes O(n) time.
    - Overall, the time complexity is O(nlogn).

Space Complexity: O(n)
    - The space complexity is O(n) to store the merged intervals.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals by their start times
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current interval does not overlap with the previous
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # there is an overlap, so we merge the current and previous intervals
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
