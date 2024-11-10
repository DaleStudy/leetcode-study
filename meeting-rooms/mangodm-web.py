from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        - Idea: 모든 회의에 참석할 수 있으려면, 앞서 오는 회의가 끝나는 시간이
            다음 회의의 시작 시간을 넘어서는 안된다.
            이를 확인하기 위해 주어진 회의 일정을 시작 시간 기준으로 정렬하고,
            순차적으로 비교하여 위의 조건을 위반하는 회의가 있는지 확인한다.
        - Time Complexity: O(nlogn). n은 회의의 수.
            정렬에 O(nlogn)이 소요되고, 순차 탐색을 하는 데는 O(n)이 필요하다.
        - Space Complexity: O(1).
            추가 공간은 사용하지 않는다.
        """
        intervals.sort()

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True
