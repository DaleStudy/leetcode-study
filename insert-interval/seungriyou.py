# https://leetcode.com/problems/insert-interval/

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        [Complexity]
            - TC: O(n)
            - SC: O(n)

        [Approach]
            intervals의 각 interval에 대해 다음의 케이스로 나눠볼 수 있다.
                1) left에 해당하는 interval: left에 추가
                2) right에 해당하는 interval: right에 추가
                3) newInterval과 겹치는 interval: ns & ne 업데이트 (newInterval 확장)
        """
        ns, ne = newInterval

        # left:     end < ns
        # right:    start > ne
        left, right = [], []

        for s, e in intervals:
            # 1) left에 해당하는 interval이라면, left에 추가
            if e < ns:
                left.append([s, e])

            # 2) right에 해당하는 interval이라면, right에 추가
            elif s > ne:
                right.append([s, e])

            # 3) newInterval과 겹치는 interval이라면, ns & ne 업데이트
            else:
                ns = min(ns, s)
                ne = max(ne, e)

        # left.append([ns, ne])
        # left.extend(right)
        # return left
        return left + [[ns, ne]] + right
