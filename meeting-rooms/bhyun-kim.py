"""
252. Meeting Rooms
https://leetcode.com/problems/meeting-rooms/

Solution:
    This is a sorting problem that requires comparing intervals.
    We can sort the intervals by the start time.
    Then, we can iterate through the sorted intervals and check if the end time of the current interval is greater than the start time of the next interval.
    If it is, then we return False.
    Otherwise, we return True.
    
    1. Sort the intervals by the start time.
    2. Iterate through the sorted intervals.
    3. Check if the end time of the current interval is greater than the start time of the next interval.


Time complexity: O(nlogn)
Space complexity: O(1)

Discarded solution:
    This solution uses a hash table to store the time table of the intervals.
    We iterate through the intervals and check if there is any overlap in the time table.

    1. Create a hash table to store the time table of the intervals.
    2. Iterate through the intervals.
    3. Check if there is any overlap in the time table.
    4. Return False if there is an overlap, otherwise return True.

Time complexity: O(n^2)
Space complexity: O(n)

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        time_table = defaultdict(int)
        for itrv in intervals: 
            for i in range(itrv[0], itrv[1]):
                if time_table[i] == 0:
                    time_table[i] += 1 
                else:
                    return False 
        return True
"""


from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
