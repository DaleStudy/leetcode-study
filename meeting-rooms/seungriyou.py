# https://leetcode.com/problems/meeting-rooms/

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        [Complexity]
            - TC: O(nlogn)
            - SC: O(1) (inplace sorting)

        [Approach]
            intervals를 start 기준으로 오름차순 정렬 후, 앞 회의의 끝 시간 > 뒷 회의의 시작 시간이라면 겹치는 것이므로 False 반환
        """
        # sort intervals (by start)
        intervals.sort()

        for i in range(1, len(intervals)):
            # prev_e > curr_s 라면 False
            if intervals[i - 1][1] > intervals[i][0]:
                return False

        return True
