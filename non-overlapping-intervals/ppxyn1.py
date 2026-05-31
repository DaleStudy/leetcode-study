# idea: - 
# Time Complexity: O(n log n)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cnt = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                cnt += 1
                prevEnd = min(end, prevEnd)
        return cnt


