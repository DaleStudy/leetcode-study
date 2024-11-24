from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])

        start_pointer, end_pointer = 0, 0
        used_rooms = 0

        while start_pointer < len(intervals):
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_times[start_pointer] >= end_times[end_pointer]:
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect.
            # used_rooms would remain the same in that case.
            used_rooms += 1
            start_pointer += 1

        return used_rooms
