"""
https://leetcode.com/problems/merge-intervals/description/

문제 설명:
- 주어진 구간(interval) 리스트에서 겹치는 구간들을 병합(merge)하여 반환합니다.
- 각 구간은 [start, end] 형태입니다.
- 결과는 겹치는 구간이 없는 리스트여야 하며, 정렬된 순서로 반환합니다.

TC: O(N log N)
- intervals를 정렬하는 데 O(N log N)
- 한 번의 반복으로 병합 처리 → O(N)

SC: O(N)
- 결과 리스트(output)에 최대 N개의 구간이 저장될 수 있음
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        for interval in sorted(intervals):
            # output이 비어있거나, 현재 interval이 이전 interval과 겹치지 않으면 그대로 추가
            if not output or output[-1][1] < interval[0]:
                output.append(interval)
            else:
                # 겹치는 경우: 끝나는 부분을 더 긴 쪽으로 병합
                output[-1][1] = max(output[-1][1], interval[1])
        
        return output
