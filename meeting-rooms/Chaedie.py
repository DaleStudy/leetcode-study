"""
Solution: 
    1) 정렬
    2) prev endTime 이 cur startTime 보다 큰 경우가 있으면 return False
Time: O(n)
Space: O(1)
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:
                return False

        return True
