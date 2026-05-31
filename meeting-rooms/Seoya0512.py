'''
Time Complexity: O(N log N)
- intervals.sort() 는 O(N log N) 소요
- for loop 는 O(N) 소요
- 전체적으로 O(N log N) + O(N) = O(N log N)

Space Complexity: O(1)
- end_time, start_time 상수 변수 추가로 사용
'''
def can_attend_meetings(self, intervals: List[Interval]) -> bool:
  intervals.sort()
  end_time = intervals[0][1]

  for i in range(1, len(intervals)):
    start_time = intervals[i][0]
    if end_time > start_time:
      return False
    end_time = intervals[i][1]
  return True
