"""
시간 복잡도: O(NLogN)
  - intervals 리스트를 정렬하기 때문입니다.
공간 복잡도: O(N)
  - 정렬 시 추가 메모리(새로운 배열)가 사용될 수 있습니다.

주어진 intervals(회의 시간표)들이 서로 겹치는지 확인하는 코드입니다.
intervals를 시작 시간 순으로 정렬한 뒤,
이전 회의의 종료 시간(final)과 현재 회의의 시작 시간(start)을 비교하여
회의가 겹치는 경우가 있는지 검사합니다.
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        final = -1

        for start, end in intervals:
            if start >= final:
                final = end
            else:
                return False

        return True
