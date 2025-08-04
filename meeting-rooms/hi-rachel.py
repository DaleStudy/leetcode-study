# https://leetcode.com/problems/meeting-rooms/
# 주어진 회의 시간 리스트에서 모든 회의가 겹치지 않고 진행될 수 있는지 확인
# 회의 시간은 [start, end] 형태의 리스트로 주어짐
# 회의 시간이 겹치는 경우 false, 겹치지 않는 경우 true 반환

# TC: O(N log N), N은 회의의 개수, 회의 시간 정렬 O(N log N)
# SC: O(1)

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            # 현재 회의의 시작 시간이 이전 회의의 종료 시간보다 작으면 겹침
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True

# sol = Solution()
# print(sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
# print(sol.canAttendMeetings([[7, 10], [2, 4]]))
