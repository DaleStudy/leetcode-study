"""
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/

Solution:
    To solve this problem, we can follow the following steps:
    1. Sort the intervals based on their start times.
    2. Initialize a list called room_times with a dummy interval.
    3. Iterate through the intervals and assign each meeting to a room.
    4. If a meeting can be assigned to an existing room, update the room's end time.
    5. If a meeting cannot be assigned to an existing room, add a new room.
    6. Return the number of rooms used.

Time Complexity: O(nlogn)
    - Sorting the intervals takes O(nlogn) time.
    - Iterating through the intervals takes O(n) time.
    - Overall, the time complexity is O(nlogn).

Space Complexity: O(n)
    - We are using a list to store the room times.
"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        room_times = [[-1, -1]]
        meet_idx = 0

        while meet_idx < len(intervals):
            m_t = intervals[meet_idx]
            found_room = False
            for i in range(len(room_times)):
                r_t = room_times[i]
                if m_t[0] >= r_t[1]:
                    room_times[i] = m_t
                    found_room = True
                    break

            if not found_room:
                room_times.append(m_t)
            meet_idx += 1

        return len(room_times)
