# N is the number of intervals.
# TC: O(N log N) - sorting the intervals by start time
# SC: O(1) - constant extra space


class Solution:

    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True
