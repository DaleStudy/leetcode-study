# TC: O(n), SC: O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)

        e = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < e:
                return False
            e = intervals[i].end

        return True
