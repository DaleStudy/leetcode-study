class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        last_end = -math.inf
        overlap_count = 0

        sorted_intervals = sorted(intervals, key=lambda interval: interval[1])

        for start, end in sorted_intervals:
            if start >= last_end:
                last_end = end
            else:
                overlap_count += 1

        return overlap_count

        ## TC: O(nlogn), SC: O(n)
