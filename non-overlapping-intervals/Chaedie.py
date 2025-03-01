"""
Solution: 직접 풀지 못해 해설을 통해 이해하고 풀었습니다. 
    Interval 문제가 계속 어렵네요.. 😂
Time: O(n)
Space: O(1)
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
