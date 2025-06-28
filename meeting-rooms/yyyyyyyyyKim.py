from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        
        # 시간복잡도(O(n^2)), 공간복잡도 O(1)
        # 시작점을 기준으로 정렬(선택정렬)
        for i in range(len(intervals)):
            idx = i
            for j in range(i+1,len(intervals)):
                if intervals[j].start < intervals[idx].start:
                    idx = j
            if idx != i:
                intervals[i], intervals[idx] = intervals[idx], intervals[i]

        # 겹치는 회의 있는지 확인
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False

        return True
