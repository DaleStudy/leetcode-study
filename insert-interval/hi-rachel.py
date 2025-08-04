# https://leetcode.com/problems/insert-interval/
# 
# 새로운 구간을 기존의 정렬된 구간 리스트에 삽입하고, 겹치는 구간을 병합
# 오름차순 정렬된 [start, end] 형태의 리스트.
# 새로운 interval [newStart, newEnd]를 삽입한 후에도 구간이 겹치지 않고 정렬된 상태로 유지.
# 
# TC: O(N), 각 interval을 최대 한 번씩만 탐색
# SC: O(N)

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # 1. 왼쪽에 있는 겹치지 않는 구간
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # 2. 겹치는 구간 병합
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # 3. 오른쪽에 있는 겹치지 않는 구간
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
