from typing import List


# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

# 7기 풀이
# 시간 복잡도: O(n log n)
# - python sorting을 이용하여 정렬하기 때문에
# 공간 복잡도: O(1)
# - 메서드 파라미터 이외에 사용하는 변수 없음
class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # intervals를 정렬, 이때 key는 각 요소의 start 시간을 기준으로 오름차순 해준다.
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            # 현재 interval 시작 시간이 이전 interval 종료 시간보다 작으면
            # 두 구간은 겹치는 구간이므로, 문제 요건에 따라 False를 early return
            if intervals[i].start < intervals[i - 1].end:
                return False
        
        # 모든 interval 구간 확인 후 겹치지 않으며
        # True를 return
        return True
