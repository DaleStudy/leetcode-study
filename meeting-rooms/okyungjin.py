# 252. Meeting Rooms
# https://www.lintcode.com/problem/920/

"""
문제:
    - 회의 시간 구간 `[start, end)` 목록이 주어진다. (start < end)
    - 한 사람이 모든 회의에 참석할 수 있는지 True/False로 반환한다.
    - 한 회의가 끝나는 시각에 다른 회의가 시작하는 것은 충돌이 아니다.

복잡도:
    n: `intervals`의 길이
    Time: O(n log n)
    Space: O(n)
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.end)

        last_end = 0
        for interval in intervals:
            if interval.start < last_end:
                return False
            last_end = interval.end
        return True
