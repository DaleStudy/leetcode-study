from typing import (
    List,
)

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            current = intervals[i]

            if prev.end > current.start:
                return False
        
        return True
