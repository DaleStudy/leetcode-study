"""
구간이 겹쳐 삭제해야 되는 최소 구간의 수를 반환해라
-> Greedy
-> '겹치지 않게 최대한 많은 구간을 남기고, 나머지를 제거'

문제 풀이
1. 끝나는 시간 기준으로 오름차순 정렬
2. 이전 구간의 끝과 현재 구간의 시작을 비교
3. 겹치면 현재 구간을 제거

TC: O(n log n), 정렬 O(n log n) + 모든 interval 한 번씩 순회 O(n) 
SC: O(1)
"""

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 끝나는 시간이 빠른 순으로 정렬
        # -> 일찍 끝나는 구간을 선택하면, 이후에 더 많은 구간을 넣을 수 있는 여지가 커짐!
        intervals.sort(key=lambda x: x[1])

        # 첫 구간 선택
        prev_end = float('-inf')  # 음의 무한대로 비교의 기준값 가장 작게 설정 -> 첫 번째 구간 무조건 선택됨
        count = 0

        # 하나씩 검사
        for start, end in intervals:
            if start >= prev_end:
                # 겹치지 않음 -> 그대로 유지
                prev_end = end
            else:
                # 겹침 -> 하나 제거
                count += 1
        
        return count
