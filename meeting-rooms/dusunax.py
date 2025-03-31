'''
# 252. Meeting Rooms

- 각 회의는 시작 시간과 종료 시간을 가진다.
- 회의 시간이 겹치는 경우 회의를 진행할 수 없다.
- 회의 시간이 겹치지 않는 경우 회의를 진행할 수 있다.

## 풀이
- intervals를 시작 시간으로 정렬한다.
- 시간 겹침 여부를 확인한다.
- 겹치는 경우 False, 겹치지 않는 경우 True를 반환한다.

## 시간 & 공간 복잡도

### TC is O(n log n)
- 정렬 시간: O(n log n)
- 겹침 여부 확인 시간: O(n)

### SC is O(1)
- 추가 사용 공간 없음
'''
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
            
        return True
