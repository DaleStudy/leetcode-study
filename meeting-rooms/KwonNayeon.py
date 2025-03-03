"""
Constraints:
- 0 ≤ intervals.length ≤ 10^4
- intervals[i].length == 2
- 0 ≤ start_i < end_i ≤ 10^6
- [(0,8), (8,10)] is not conflict at 8

Time Complexity: O(nlogn)
- 정렬에 nlogn, 순회에 n이 필요하므로 전체는 O(nlogn)

Space Complexity: O(1)
- 정해진 개수의 변수 외에는 추가 공간을 사용하지 않음

풀이방법:
1. Base case: 빈 배열/none일 때 True 반환
2. intervals를 시작점 기준으로 정렬
3. prev_end 초기화 (첫 번째 미팅의 종료 시간)
4. 두 번째 미팅부터 순회하면서:
  - 만약 현재 시작점 (미팅 시작 시간)이 이전 미팅의 종료 시간보다 작으면 false 반환
  - 그렇지 않으면 prev_end를 현재 미팅의 종료 시간으로 업데이트
5. 모든 미팅을 검사한 후에도 충돌이 없으면 true 반환
"""
from typing import List

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        
        intervals.sort(key=lambda x: x.start)
        
        prev_end = intervals[0].end
        
        for interval in intervals[1:]:

            if interval.start < prev_end:
                return False
            prev_end = interval.end
        
        return True

