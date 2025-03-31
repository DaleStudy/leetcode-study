# Time Complexity: O(N log N) - sorting the intervals takes O(N log N), and the iteration takes O(N).
# Space Complexity: O(1) - sorting is done in place, and we use only a few extra variables.

class Solution:
    def can_attend_meetings(intervals):
        if not intervals:
            return True  

        # sort intervals based on start times
        intervals.sort()  # O(N log N) sorting

        # check for overlapping meetings
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:  
                # if the current meeting's end time is later than the next meeting's start time, have a conflict
                return False

        # no conflicts found, all meetings can be attended
        return True 
