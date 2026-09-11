# N is the number of intervals.
# TC: O(N log N) - sorts intervals by end time and performs a single pass
# SC: O(N) - space required for sorting


class Solution:

    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        remove_count = 0
        prev_end = float("-inf")

        for start, end in intervals:
            if start < prev_end:
                remove_count += 1
            else:
                prev_end = end

        return remove_count
