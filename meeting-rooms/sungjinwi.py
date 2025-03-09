"""
    
"""

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
        sorted_interval = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(sorted_interval)) :
            if sorted_interval[i].start < sorted_interval[i - 1].end:
                return False
        return (True)
