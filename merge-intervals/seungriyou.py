# https://leetcode.com/problems/merge-intervals/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [Complexity]
            - TC: O(nlogn) (sorting)
            - SC: O(1) (res 제외)

        [Approach]
            intervals를 오름차순 정렬하면, 이를 순회하면서 끝 값만 비교하며 interval이 서로 겹치는 경우와 겹치지 않는 경우를 판단할 수 있다.
            이전 interval과 겹치는 경우라면, 이전 끝 값과 현재 끝 값 중 큰 값으로 업데이트하면 된다.
        """
        res = []

        # interval의 시작 값이 작은 순으로 정렬
        # -> intervals를 순회하며 끝 값만 비교하며 non-overlapping/overlapping interval 판단 가능
        intervals.sort()

        for s, e in intervals:
            # (1) non-overlapping: res가 비었거나, 이전 e < 현재 s인 경우 -> 그대로 추가
            if not res or res[-1][1] < s:
                res.append([s, e])
            # (2) overlapping: 이전 e >= 현재 s인 경우 -> 이전 e와 현재 e 중 큰 값으로 업데이트
            else:
                res[-1][1] = max(res[-1][1], e)

        return res
