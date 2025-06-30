# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List

class Solution:
    def eraseOverlapIntervals1(self, intervals: List[List[int]]) -> int:
        """
        [Complexity]
            - TC: O(nlogn) (sort)
            - SC: O(1) (tim sort -> 최악의 경우 O(n)까지 가능)

        [Approach]
            intervals를 start 기준으로 오름차순 정렬 후, greedy 하게 항상 작은 end를 가지는 interval을 선택한다.
        """
        # sort asc by start
        intervals.sort(key=lambda x: x[0])

        # initialize prev_e
        prev_e = intervals[0][0] - 1
        to_be_removed = 0

        for s, e in intervals:
            # (1) overlapping       : greedy하게 prev_e와 e 중 더 작은 값으로 prev_e를 업데이트하고, 제거할 interval 수 증가
            if prev_e > s:
                prev_e = min(prev_e, e)
                to_be_removed += 1
            # (2) non-overlapping   : prev_e만 업데이트
            else:
                prev_e = e

        return to_be_removed

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [Complexity]
            - TC: O(nlogn) (sort)
            - SC: O(1) (tim sort -> 최악의 경우 O(n)까지 가능)

        [Approach]
            이전 풀이의 (1) overlapping 단계에서 prev_e와 e 중 min을 고르는 로직을 제거하려면, intervals를 end 기준으로 오름차순 정렬하면 된다.
        """
        # sort asc by end
        intervals.sort(key=lambda x: x[1])

        # initialize prev_e
        prev_e = intervals[0][0] - 1
        to_be_removed = 0

        for s, e in intervals:
            # (1) overlapping       : greedy하게 prev_e와 e 중 더 작은 값으로 선택하면 되므로 prev_e를 그대로 두고, 제거할 interval 수 증가
            if prev_e > s:
                to_be_removed += 1
            # (2) non-overlapping   : prev_e만 업데이트
            else:
                prev_e = e

        return to_be_removed
