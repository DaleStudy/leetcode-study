class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cnt = 0
        pre_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if pre_end > start:
                cnt += 1
                pre_end = min(end, pre_end)
            else:
                pre_end = end
        return cnt
