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
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:

        # 투포인터
        # 시간복잡도 O(n log n) , 공간복잡도 O(n) 

        # 시작 시간과 종료 시간을 각각 정렬
        s = sorted([i.start for i in intervals])
        e = sorted([i.end for i in intervals])

        s_pointer = e_pointer = 0
        rooms = max_rooms = 0

        while s_pointer < len(intervals):
            
            # 기존 회의가 끝나기 전에 새로운 회의 시작(새로운 방 필요)
            if s[s_pointer] < e[e_pointer]:
                rooms += 1
                s_pointer += 1
            # 기존 회의 종료(방 퇴실)
            else:
                rooms -= 1
                e_pointer += 1

            # 지금까지 필요한 방의 최대값을 갱신
            max_rooms = max(max_rooms, rooms)

        return max_rooms

