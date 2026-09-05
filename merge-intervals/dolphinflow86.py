# N is the number of intervals.
# TC: O(N log N) - sorts intervals by start time and merges in a single pass
# SC: O(N) - space for the output array and sorting


class Solution:

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)

        return merged
