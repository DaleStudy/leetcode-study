'''
시간 복잡도: O(n log n)
- intervals 정렬하는 데 O(n log n)
- intervals 한 번 순회하면서 병합 작업 수행: O(n)

공간 복잡도: O(n)
- 결과 리스트에 병합된 interval을 저장해야 하므로 O(n)
'''
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        left, right = intervals[0]

        for start, end in intervals[1:]:
            # stop merging
            if 0 <= right < start:
                result.append([left, right])
                left, right = start, end
            # merge overlapping intervals
            else:
                left, right = min(left, start), max(right, end)

        result.append([left, right])
        
        return result
